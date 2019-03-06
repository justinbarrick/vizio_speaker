import sys
import asyncio
import functools


SERVICE = 'vizio_speaker'
REQUIREMENTS = ['pyvizio-speaker==0.0.1']


def start_loop(func):
    @functools.wraps(func)
    def new_func(*args, **kwargs):
        loop = asyncio.new_event_loop()
        loop.run_until_complete(func(*args, **kwargs))

    return new_func


@start_loop
async def call_method(speaker, method, *args):
    resp = await getattr(speaker, method)(*args)

    if not isinstance(resp, pyvizio_speaker.Response):
        return

    for item in resp.items.as_list():
        print(item)


def setup(hass, config):
    import pyvizio_speaker

    def speaker():
        return pyvizio_speaker.Speaker(config['vizio_speaker']['host'])

    @start_loop
    async def handle_set_input(call):
        await speaker().set_input(call.data['input'])

    @start_loop
    async def handle_set_volume(call):
        await speaker().set_volume(call.data['volume'])

    @start_loop
    async def handle_volume_up(call):
        await speaker().volume_down()

    @start_loop
    async def handle_volume_down(call):
        await speaker().volume_up()

    @start_loop
    async def handle_mute(call):
        await speaker().mute()

    @start_loop
    async def handle_unmute(call):
        await speaker().unmute()

    @start_loop
    async def handle_toggle_mute(call):
        await speaker().mute_toggle()

    @start_loop
    async def handle_power_on(call):
        s = speaker()
        await s.update_power_state()
        await s.power_on()

    @start_loop
    async def handle_power_off(call):
        s = speaker()
        await s.update_power_state()
        await s.power_off()

    @start_loop
    async def handle_toggle_power(call):
        await speaker().power_toggle()

    hass.services.register(SERVICE, 'set_input', handle_set_input)
    hass.services.register(SERVICE, 'set_volume', handle_set_volume)
    hass.services.register(SERVICE, 'volume_up', handle_volume_up)
    hass.services.register(SERVICE, 'volume_down', handle_volume_down)
    hass.services.register(SERVICE, 'mute', handle_mute)
    hass.services.register(SERVICE, 'unmute', handle_unmute)
    hass.services.register(SERVICE, 'toggle_mute', handle_toggle_mute)
    hass.services.register(SERVICE, 'power_on', handle_power_on)
    hass.services.register(SERVICE, 'power_off', handle_power_off)
    hass.services.register(SERVICE, 'toggle_power', handle_toggle_power)

    print('Loaded vizio_speaker')
    return True


if __name__ == '__main__':
    import pyvizio_speaker
    speaker = pyvizio_speaker.Speaker(sys.argv[1])
    call_method(speaker, sys.argv[2], *sys.argv[3:])
