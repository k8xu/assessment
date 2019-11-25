import odio_urdf
import numpy as np
import pybullet as p
import time

def transformation(pos, translation_vec, quat, inverse=False):
    """ Converts a position from one frame to another
    :param p: vector of length 3, position (x,y,z) in frame original frame
    :param translation_vec: vector of length 3, (x,y,z) from original frame to desired frame
    :param quat: vector of length 4, (x,y,z,w) rotation from original frame to desired frame
    :param inverse (optional): if True, inverts the translation_vec and quat
    """
    if inverse:
        translation_vec, quat = p.invertTransform(translation_vec, quat)
    R = p.getMatrixFromQuaternion(quat)
    R = np.reshape(R, (3,3))
    T = np.zeros((4,4))
    T[:3,:3] = R
    T[:3,3] = translation_vec
    T[3,3] = 1.0
    pos = np.concatenate([pos, [1]])
    new_pos = np.dot(T, pos)
    return new_pos[:3]

def vis_frame(pos, quat, length=0.2, lifeTime=0.4):
    """ This function visualizes a coordinate frame for the supplied frame where the
    red,green,blue lines correpsond to the x,y,z axes.
    :param p: a vector of length 3, position of the frame (x,y,z)
    :param q: a vector of length 4, quaternion of the frame (x,y,z,w)
    """
    new_x = transformation([length, 0.0, 0.0], pos, quat)
    new_y = transformation([0.0, length, 0.0], pos, quat)
    new_z = transformation([0.0, 0.0, length], pos, quat)

    p.addUserDebugLine(pos, new_x, [1,0,0], lifeTime=lifeTime)
    p.addUserDebugLine(pos, new_y, [0,1,0], lifeTime=lifeTime)
    p.addUserDebugLine(pos, new_z, [0,0,1], lifeTime=lifeTime)

def object_to_urdf(object_name, object):
    rgb = np.random.uniform(0, 1, 3)
    link_urdf = odio_urdf.Link(object_name,
                  odio_urdf.Inertial(
                      odio_urdf.Origin(xyz=object.com, rpy=(0, 0, 0)),
                      odio_urdf.Mass(value=object.mass),
                      odio_urdf.Inertia(ixx=0.001,
                                        ixy=0,
                                        ixz=0,
                                        iyy=0.001,
                                        iyz=0,
                                        izz=0.001)
                  ),
                  odio_urdf.Collision(
                      odio_urdf.Origin(xyz=(0, 0, 0), rpy=(0, 0, 0)),
                      odio_urdf.Geometry(
                          odio_urdf.Box(size=(object.dimensions.width,
                                                object.dimensions.length,
                                                object.dimensions.height))
                      )
                  ),
                  odio_urdf.Visual(
                      odio_urdf.Origin(xyz=(0, 0, 0), rpy=(0, 0, 0)),
                      odio_urdf.Geometry(
                          odio_urdf.Box(size=(object.dimensions.width,
                                                object.dimensions.length,
                                                object.dimensions.height))
                      ),
                      odio_urdf.Material('color',
                                    odio_urdf.Color(rgba=(*object.color, 1.0))
                                    )
                  ))

    object_urdf = odio_urdf.Robot(link_urdf)
    return object_urdf

def render_objects(objects, obj_ps, time_steps=500, vis_frames=False):
    client = p.connect(p.GUI)
    p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)
    p.configureDebugVisualizer(p.COV_ENABLE_MOUSE_PICKING, 0)
    p.resetDebugVisualizerCamera(
        cameraDistance=.4,
        cameraYaw=45,
        cameraPitch=-45,
        cameraTargetPosition=(0., 0., 0.))
    p.setGravity(0, 0, -10)

    obj_models = []
    for obj in obj_ps:
        if obj == 'ground':
            plane_id = p.loadURDF("plane_files/plane.urdf", obj_ps[obj])
        else:
            object_urdf = object_to_urdf(obj, objects[obj])
            with open(obj+'.urdf', 'w') as handle:
                handle.write(str(object_urdf))
            obj_model = p.loadURDF(obj+'.urdf', obj_ps[obj])
            obj_models.append(obj_model)
            if vis_frames:
                pos,quat = p.getBasePositionAndOrientation(obj_model, 0)
                vis_frame(pos, quat, lifeTime=1000)

    for t in range(time_steps):
        p.stepSimulation()
        time.sleep(.001)
    p.disconnect()
