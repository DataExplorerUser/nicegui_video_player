# Example of a video player that automatically adjusts to
# the height and width of the window (viewport) when running
# a NiceGUI app in desktop (native) mode or in a browser. The
# video player always shows the video at its maximum size
# while never cutting off either the bottom or right side of
# the video.

from nicegui import ui, context

# Let the content of the current client grow to 100% view
# height (100vh). This turns an infinitely scrolling webpage
# into a single screen only. Based on this comment by Falko-s:
# www.reddit.com/r/nicegui/comments/17wl8ar/

context.get_client().content.classes('h-[100vh]')

# Add CSS for the div surrounding the video player and the
# video player itself. CSS based on the following post by ADTC.
# https://stackoverflow.com/a/77748185

ui.add_head_html('''
<style>
.video_container {
  position: relative;
  width: 100%;
  height: 100%;
}

.video {
  position: absolute;
  width: 100%;
  height: 100%;
  object-fit: contain;
}
</style>
''')

# ui.row acts as the div to which the custom CSS is applied.
with ui.row().classes('video_container'):
    v = ui.video(src='video.mp4').classes('video')

ui.run(native=True, fullscreen=False)