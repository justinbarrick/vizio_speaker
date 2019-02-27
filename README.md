A Home Assistant component for controlling a Vizio smart speaker.

To setup, copy `__init__.py` to `$CONFIG/custom_components/__init__.py`, update
`configuration.yaml` with the IP of your smart speaker, and restart Home Assistant.

```
vizio_speaker:
  host: 10.0.0.226
```

You can then use the `vizio_speaker` services:

* `set_input`: set the speaker's input, the argument is a json dictionary with the
               "input" field set to the input to load (e.g., `{"input":"HDMI-ARC"}`).
* `set_volume`: set the speaker's volume, the argument is a json dictionary with the
               "volume" field set to the desired volume (e.g., `{"input":6}`). Volume
               appears to be an integer between 0-15.
* `volume_up`: increase the volume
* `volume_down`: decrease the volume
* `mute`: mute the speaker
* `unmute`: unmute the speaker
* `toggle_mute`: toggle mute on the speaker
* `power_on`: turn on the speaker
* `power_off`: turn off the speaker
* `toggle_power`: toggle the speaker's power
