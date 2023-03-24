#import glob
import glob
#import os
import glob
#import sys
import sys
#import argparse
import argparse
import random
#import time
import time
try:
    sys.path.append(glob.glob('../carla/dist/carla-*%d.%d-%s.egg' % (
        sys.version_info.major,
        sys.version_info.minor,
        'win-amd64' if os.name == 'nt' else 'linux-x86_64'))[0])
except IndexError:
    pass

#import carla
import carla
#create a list name actor_list
actor_list=[]
def main(arg):
    """Main function of the script"""
    #python script for host and port declaration and put in client variable
    client = carla.Client(arg.host, arg.port)
    #Time to wait for screen
    client.set_timeout(10.0)
    #Define get_world() method and save in world variable
    world = client.get_world()

    #define try
    try:

        #define blueprint of world
        blueprint_library = world.get_blueprint_library()
        #vehicle model
        vehicle_bp = blueprint_library.filter(arg.filter)[0]

        #location for the vehicle
        vehicle_transform = world.get_map().get_spawn_points()[133]
        vehicle_transform.location.z += 3
        vehicle = world.spawn_actor(vehicle_bp, vehicle_transform) #call vehicle with variable name dropped_vehicle
        vehicle.set_autopilot() #set vehicle as autopilot

        spectator_transform = carla.Transform(vehicle_transform.location, vehicle_transform.rotation)
        spectator_transform.location += vehicle_transform.get_forward_vector() * 20
        spectator_transform.rotation.yaw += 180
        spectator = world.get_spectator()
        spectator.set_transform(spectator_transform)
        vehicle.set_transform(vehicle_transform)
        actor_list.append(dropped_vehicle)

        #put time in sleep for 1000
        time.sleep(1000)


    finally:
        print('destroying actors')
        #create a loop for actor in actor_list
            #actor every actor
        print('done.')


