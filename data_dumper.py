import Leap
import sys
import json
import time
import datetime


class FrameData:
    def __init__(self, frame):
        self.frame = frame

    def to_json_obj(self):
        frame = self.frame

        frame_dict = {}
        frame_dict['id'] = frame.id
        frame_dict['timestamp'] = frame.timestamp
        frame_dict['hand_count'] = len(frame.hands)
        frame_dict['finger_count'] = len(frame.fingers)
        frame_dict['tool_count'] = len(frame.tools)
        frame_dict['hands'] = []

        if not frame.hands.empty:
            for hand in frame.hands:
                hand_dict = {}

                fingers = hand.fingers
                hand_dict['fingers'] = []
                hand_dict['finger_count'] = len(fingers)
                if not fingers.empty:
                    for finger in fingers:
                        hand_dict['fingers'].append(finger.tip_position)

                hand_dict['sphere_radius'] = hand.sphere_radius
                hand_dict['sphere_center'] = hand.sphere_center

                hand_dict['palm_position'] = hand.palm_position
                hand_dict['paml_velocity'] = hand.palm_velocity

                # Get the hand's normal vector and direction
                normal = hand.palm_normal
                direction = hand.direction

                hand_dict['palm_normal'] = normal
                hand_dict['direction'] = direction

                # Calculate the hand's pitch, roll, and yaw angles
                hand_dict['pitch'] = direction.pitch * Leap.RAD_TO_DEG
                hand_dict['roll'] = normal.roll * Leap.RAD_TO_DEG
                hand_dict['yaw'] = direction.yaw * Leap.RAD_TO_DEG

                frame_dict['hands'].append(hand_dict)

        return frame_dict


class FrameEncoder(json.JSONEncoder):
    def dump_leap_vector(self, vector):
        result = {}
        result['x'] = vector.x
        result['y'] = vector.y
        result['z'] = vector.z
        result['pitch'] = vector.pitch
        result['roll'] = vector.roll
        result['yaw'] = vector.yaw
        return result

    def default(self, obj):
        if isinstance(obj, FrameData):
            return obj.to_json_obj()
        elif isinstance(obj, Leap.Vector):
            return self.dump_leap_vector(obj)

        return super(FrameEncoder, self).default(obj)


class DataDumperListener(Leap.Listener):
    def __init__(self):
        super(DataDumperListener, self).__init__()
        self.data_buffer = []

    def on_frame(self, controller):
        # Get the most recent frame and report some basic information
        frame = controller.frame()
        self.data_buffer.append(FrameData(frame))

        # Give some feedback to user
        print "Frame id: %d, timestamp: %d, hands: %d, fingers: %d, tools: %d, gestures: %d" % (
              frame.id, frame.timestamp, len(frame.hands), len(frame.fingers), len(frame.tools), len(frame.gestures()))


def main():
    # Create a sample listener and controller
    listener = DataDumperListener()
    controller = Leap.Controller()

    print "Press Enter to start tracking, press Enter again to stop..."
    sys.stdin.readline()

    controller.add_listener(listener)

    sys.stdin.readline()

    print "Dumping..."
    result = json.dumps(listener.data_buffer, cls=FrameEncoder, sort_keys=True, indent=4, separators=(',', ': '))
    filename = "data-" + str(time.mktime(datetime.datetime.now().timetuple()))[:-2] + ".json"
    f = open(filename, "w")
    f.write(result)

    # Remove the sample listener when done
    controller.remove_listener(listener)

    print "Done!"


if __name__ == "__main__":
    main()
