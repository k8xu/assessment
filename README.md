# Research Problem

Robotic manipulation tasks require robots to reason about how to use their end effectors, or hands, to grasp and move objects around the world. I am interested in tasks that require some physical understanding of the world. This includes tasks like balancing objects in specific arrangements, moving constrained mechanisms such as doors, and/or tool use problems. In the example of stacking objects, the physical understanding of an object’s center of mass (COM) is important so that the objects don't fall. Other physical concepts such as friction are important, but for this assignment we will focus on COM and stability. The objective of this assignment is to familiarize you with a simple notion of object stability and to visualize solutions to finding stable arrangements of objects in a simulator.

If any part of this problem interests you, try out the assignment below. Please dedicate at most 8 hours to it, and turn in what you have completed in that time. I encourage you to reach out to me at carism@mit.edu if you have any questions!

## Course Prerequisites

Students applying and completing this assignment should have completed courses 6.006 and 6.009. If you feel that you are a good fit but have not completed these courses please email me and we can discuss.

## Directions

### Requirements

- Python 3.7 (probably will work with earlier versions, but try to use this version)
- pip3
- git

### Install Instructins

I ran everything on a Mac, but I can try to help debug platform issues.

1. Fork this repository into your GitHub account, clone it, and cd into it
2. Run ```pip3 install .``` to get dependencies
3. Run ```pip3 install git+https://github.com/hauptmech/odio_urdf``` (another dependency)
4. Run ```jupyter notebook assignment.ipynb``` to launch a notebook in a browser
5. Fill in the required coding portions and questions
6. When you are finished, commit and push your answers to your fork. Send me an email linking to your repo. You can either add me as a collaboarator or make the repo public.
