#!/usr/bin/env -S PYTHONPATH=../telemetry python3

from telemetry.config_log import *
from high_stakes.events import *

# Open log based on config
config_open_log()


def driver_function():
    """Function for the driver part of a competition match"""

    log(("Competition", "competition"), "driver_begin")

    # Add driver logic here
    # Note that event handling is initialized outside of this function by init_event_handling()

    log(("Competition", "competition"), "driver_end")


def autonomous_function():
    """Function for the autonomous part of a competition match"""

    log(("Competition", "competition"), "autonomous_begin")

    # robot_position.reset(Position(-1350, -600)) # use this for 2-ring
    robot_position.reset(Position(-1250, -800))  # use this for 3-ring
    # inertial.set_heading(-90) # use this for 2-ring
    inertial.set_heading(270)  # use this for 3-ring

    reset_robot_position_and_heading_to_gps()
    trigger_mover.move(Position(-970, -800), REVERSE)
    slow_trigger_mover.move(Position(-750, -690), REVERSE)

    clamp.set(True)

    # preload
    intake.spin_forward()
    wait(1000, MSEC)

    trigger_mover.move(Position(-600, -1200))
    wait(1000, MSEC)
    trigger_mover.move(Position(-430, -430))
    trigger_turner.turn(45, FRAME_ABSOLUTE)

    log(("Competition", "competition"), "autonomous_end")


# Initialize event handling
init_event_handling()

# Register the competition functions
competition = Competition(driver_function, autonomous_function)
