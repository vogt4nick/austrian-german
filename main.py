"""Functions to use with the macros plugin.

Example usage:
    ``` markdown
    {{ embed_youtube_video("B2X0NUJhT-4", "35", "62") }}
    ```

Macros Plugin Docs:
    https://mkdocs-macros-plugin.readthedocs.io/en/latest/
"""


def define_env(env):
    """This is the hook for macro functions (new form)"""

    @env.macro
    def embed_youtube_video(id: str, start: str = "", end: str = ""):
        """Embed a youtube video.

        start and end must be in seconds with no unit, e.g. start="62".
        Otherwise it won't work.
        """
        start_string = f"&start={start}" if start else ""
        end_string = f"&end={end}" if end else ""
        param_string = start_string + end_string

        # respect trailing spaces!
        # e.g. <div style="padding-bottom: 56.25%; position: relative;"><iframe style="position: absolute; top: 0px; left: 0px; width: 100%; height: 100%;" width="100%" height="100%" src="https://www.youtube-nocookie.com/embed/B2X0NUJhT-4?end=62&fs=0&playsinline=1&rel=0&start=35" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture; fullscreen" ></iframe></div>
        div = (
            '<div style="padding-bottom: 56.25%; position: relative;">'
            "<iframe "
            'style="position: absolute; top: 0px; left: 0px; width: 100%; height: 100%;" width="100%" height="100%" '
            f'src="https://www.youtube-nocookie.com/embed/{id}?fs=0&playsinline=1&rel=0{param_string}" '
            'frameborder="0" '
            'allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture; fullscreen">'
            "</iframe></div>"
        )
        # print(div)
        return div
