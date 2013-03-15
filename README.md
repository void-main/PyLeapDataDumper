# PyLeapDataDumper

Dumps frame info from leap motion

## Usage
- Plugin your leap motion device
- Launch the Leap application
- Run `python data_dumper.py`
- Press `Enter` to start tracking
- Press `Enter` again to stop tracking
- Wait for the dumper to do the work
- The result file is saved as `data-TIMESTAMP.json` (in json file format)

## Attention
Works only on mac for now

## File Format
The whole json file is nothing but a collection of frames. Take a frame with hands & fingers for example, see the following snippet:

    {
        "finger_count": 6,
        "hand_count": 1,
        "hands": [
            {
                "direction": {
                    "pitch": 0.23746386170387268,
                    "roll": -2.944460153579712,
                    "x": -0.04674945026636124,
                    "y": 0.23406752943992615,
                    "yaw": -0.04830223694443703,
                    "z": -0.9670999050140381
                },
                "finger_count": 5,
                "fingers": [
                    {
                        "pitch": 1.253741979598999,
                        "roll": 2.6186063289642334,
                        "x": 71.08364868164062,
                        "y": 123.29479217529297,
                        "yaw": 1.0533839464187622,
                        "z": -40.45591354370117
                    },
                    {
                        "pitch": 1.3662465810775757,
                        "roll": 2.927165985107422,
                        "x": 35.835323333740234,
                        "y": 164.5523223876953,
                        "yaw": 0.80967116355896,
                        "z": -34.13656234741211
                    },
                    {
                        "pitch": 1.3336200714111328,
                        "roll": 2.466625928878784,
                        "x": 94.95401763916016,
                        "y": 118.63762664794922,
                        "yaw": 1.2774895429611206,
                        "z": -28.677783966064453
                    },
                    {
                        "pitch": 1.5324352979660034,
                        "roll": 2.3551313877105713,
                        "x": 114.72560119628906,
                        "y": 114.48194885253906,
                        "yaw": 1.532516598701477,
                        "z": -4.393806457519531
                    },
                    {
                        "pitch": 1.8371875286102295,
                        "roll": -3.1375555992126465,
                        "x": -0.5004447102546692,
                        "y": 123.95965576171875,
                        "yaw": -3.1267988681793213,
                        "z": 33.825714111328125
                    }
                ],
                "palm_normal": {
                    "pitch": -1.3451777696609497,
                    "roll": -0.04256250336766243,
                    "x": -0.041319649666547775,
                    "y": -0.9702130556106567,
                    "yaw": -0.18346178531646729,
                    "z": -0.22268956899642944
                },
                "palm_position": {
                    "pitch": 1.9169327020645142,
                    "roll": 2.7287518978118896,
                    "x": 60.64589309692383,
                    "y": 138.45692443847656,
                    "yaw": 2.259638786315918,
                    "z": 49.93534469604492
                },
                "paml_velocity": {
                    "pitch": -1.8165075778961182,
                    "roll": 1.0114258527755737,
                    "x": 127.51847076416016,
                    "y": -79.83586120605469,
                    "yaw": 1.7265305519104004,
                    "z": 20.021116256713867
                },
                "pitch": 13.605677221326573,
                "roll": -2.4386518369443166,
                "sphere_center": {
                    "pitch": 1.7316354513168335,
                    "roll": 2.734736204147339,
                    "x": 49.699256896972656,
                    "y": 115.33856964111328,
                    "yaw": 1.9308959245681763,
                    "z": 18.71259117126465
                },
                "sphere_radius": 63.94282531738281,
                "yaw": -2.767514350261777
            }
        ],
        "id": 475087,
        "timestamp": 4127993378,
        "tool_count": 0
    }
    
Quite straight forward, nothing more to be explained.