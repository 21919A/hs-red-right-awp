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

    # Reset robot position and inertial heading to the starting autonomous position and heading
    robot_position.reset(Position(-1500, -1500))
    inertial.set_heading(-90)

    # Then try resetting to GPS if GPS sensor is installed and reports high quality
    reset_robot_position_and_heading_to_gps()
    
    # pid_driver.drive(300)

    intake_1st_stage.set_velocity(600, RPM)
    intake_2nd_stage.set_velocity(600, RPM)

    trigger_driver.drive(-1000)
    trigger_turner.turn(-30, FRAME_HEADING_RELATIVE)
    trigger_driver.drive(-600)
    clamp.set(True)
    trigger_turner.turn(30, FRAME_HEADING_RELATIVE)
    intake_1st_stage.spin(REVERSE)
    intake_2nd_stage.spin(FORWARD)
    trigger_driver.drive(800)
    trigger_turner.turn(70, FRAME_HEADING_RELATIVE)
    reset_robot_position_and_heading_to_gps()
    intake_retract.set(True)
    trigger_driver.drive(1250)
    trigger_turner.turn(-144, FRAME_HEADING_RELATIVE)
    intake_retract.set(False)
    reset_robot_position_and_heading_to_gps()
    trigger_driver.drive(1700)

    # intake_1st_stage.set_velocity(450, RPM)
    # intake_2nd_stage.set_velocity(450, RPM)
    # pid_driver.drive(-1080, False)

    # clamp.set(True)
    # intake_1st_stage.spin(REVERSE)
    # intake_2nd_stage.spin(FORWARD)

    # wait(1000, MSEC)
    # reset_odometry_to_gps()

    # pid_turner.turn(40, FRAME_HEADING_RELATIVE)
    # intake_retract.set(True)
    # pid_driver.drive(670)
    # intake_retract.set(False)
    # wait(50, MSEC)
    # pid_turner.turn(-148, FRAME_HEADING_RELATIVE)

    # wait(100, MSEC)
    # reset_odometry_to_gps()

    # pid_driver.drive(800, True)
    # pid_turner.turn(40, FRAME_HEADING_RELATIVE)
    # wait(50, MSEC)
    # intake_2nd_stage.stop()

    # # pid_driver.drive(-780, True)
    # wait(100, MSEC)
    # reset_odometry_to_gps()

    # wait(1000, MSEC)
    # reset_robot_position_and_heading_to_gps()

    # trigger_turner.turn(40, FRAME_HEADING_RELATIVE)
    # intake_retract.set(True)
    # trigger_driver.drive(670)
    # intake_retract.set(False)
    # wait(50, MSEC)
    # trigger_turner.turn(-148, FRAME_HEADING_RELATIVE)

    # wait(100, MSEC)
    # reset_robot_position_and_heading_to_gps()

    # trigger_driver.drive(800)
    # trigger_turner.turn(40, FRAME_HEADING_RELATIVE)
    # wait(50, MSEC)
    # intake_2nd_stage.stop()

    # # trigger_driver.drive(-780)
    # wait(100, MSEC)
    # reset_robot_position_and_heading_to_gps()
    log(("Competition", "competition"), "autonomous_end")


# Initialize event handling
init_event_handling()

# Register the competition functions
competition = Competition(driver_function, autonomous_function)
