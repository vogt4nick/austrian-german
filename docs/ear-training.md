# Ear Training

Take this practice in four stages, repeating as necessary:

1. Listen without subtitles.
2. Listen with partial subtitles in dialect and trying to comprehend the hidden words.
3. Listen with full subtitles in dialect.
4. Listen finally with full standard German subtitles to cement understanding.

!!! info "This is a demo and might not hang around."

<style>
.spoiler {
    background-color: gray;
    color: transparent;
    user-select: none;
}

.spoiler:hover {
    background-color: inherit;
    color: inherit;
}

.subtitles_at {
    display: none;
}

.subtitles_de {
    display: none;
    font-size: .83em;
    /* line-height: 0.5em; */
    vertical-align: baseline;
    position: relative;
    top: -0.4em;
}
</style>

<script>
function revealSpoiler(name) {
    var list = document.getElementsByClassName(name);
    for (var i=0, element; element = list[i]; i++) {
        element.style.backgroundColor="inherit";
        element.style.color="inherit";
        element.style.display="inline";
    }
}

function toggleSelector(selector) {
    var list = document.querySelectorAll(selector);
    for (var i=0, element; element = list[i]; i++) {
        if (element.style.display != "none") {
            element.style.display = "none";
        } else {
            element.style.display="inline";
        }
    }
}
</script>

## Exercise: Mundl

{{ embed_youtube_video("rgib5xy8MJ4", "54", "63") }}

<button href="javascript://" onclick="toggleSelector('.subtitles_at')" class="md-button">Show {{at}} subtitles</button>
<button href="javascript://" onclick="revealSpoiler('spoiler')" class="md-button">Show spoilers</button>
<button href="javascript://" onclick="toggleSelector('.subtitles_de')" class="md-button">Show {{de}} subtitles</button>

<!-- why markdown="1"? https://stackoverflow.com/questions/47165449/use-static-html-in-mkdocs -->
<div class="annotate" markdown="1">

<!-- placeholder for proper rendering -->
> :factory_worker: Prost, Oida.     <!-- class:subtitles_at -->  
> Prost, Alter.                     <!-- class:subtitles_de -->  
> :man_bald_tone1: Du sogst olle "Oida" zu mia, !!heast!!. Haaß Mundl.  <!-- class:subtitles_at -->  
> Du sagst alle "Alter" zu mir, hörst du. Ich heiße Mundl.              <!-- class:subtitles_de -->  
> :factory_worker: Servas.          <!-- class:subtitles_at -->  
> Servus.                           <!-- class:subtitles_de -->  

</div>

## Exercise: Schoafe Schoaf

{{ embed_youtube_video("B2X0NUJhT-4", "35", "62") }}

<button href="javascript://" onclick="toggleSelector('.subtitles_at')" class="md-button">Show {{at}} subtitles</button>
<button href="javascript://" onclick="revealSpoiler('spoiler')" class="md-button">Show spoilers</button>
<button href="javascript://" onclick="toggleSelector('.subtitles_de')" class="md-button">Show {{de}} subtitles</button>

<div class="annotate" markdown="1">

<!-- placeholder for proper rendering -->
> :man_tone1: Schoafe Schoaf. Danke.                    <!-- class:subtitles_at -->  
> Scharfe Scharf. Danke.                                <!-- class:subtitles_de -->  
> :woman: !!Sog!!, wos is a schoafe Schoaf?             <!-- class:subtitles_at -->  
> Sag, was ist eine "scharfe Scharf?"                   <!-- class:subtitles_de -->  
> :man_tone1: Sie !!san!! von Wien? :woman: _Ja._       <!-- class:subtitles_at -->  
> Sie sind von Wien? _Ja._                              <!-- class:subtitles_de -->  
> :man_tone1: Warum !!kennat's!! des ned? (1)           <!-- class:subtitles_at -->  
> Warum kennte sie das nicht?                           <!-- class:subtitles_de -->  
> :man_tone1: Schoafe Schoaf is a schoafe Burnwurst mid schoafm Senf. Schoaf, Schoaf.   <!-- class:subtitles_at -->  
> "Scharfe Scharf" ist eine scharfe Burenwurst mit scharfem Senf. Scharf, Scharf.       <!-- class:subtitles_de -->  
> :man_tone1: Also, !!brauch!! ma ned mehrere Sochn.    <!-- class:subtitles_at -->  
> Also, braucht man nicht mehrere Sachen.               <!-- class:subtitles_de -->  
> :man_tone1: !!Song!! so, muss aanfoch "schoaf Schoaf."<!-- class:subtitles_at -->  
> Sagen so, (es) muss einfach "scharf Scharf."          <!-- class:subtitles_de -->  
> :man_tone1: "Schoafe Schoaf" is schoafe Schoaf.       <!-- class:subtitles_at -->  
> "Scharfe Scharf" ist "scharfe Scharf."                <!-- class:subtitles_de -->  
> :man_tone1: Es is, is irgendwo verständlich, oder hob mi -- hob i mi richtig !!aufgregt!!. <!-- class:subtitles_at -->  
> Es ist, ist irgendwo verständlich, oder habe mich -- habe ich mich richtig aufgeregt.  <!-- class:subtitles_de -->  

</div>

1. The man is either speaking aside to himself for a moment (_kennat's_ as in _kennat se_) or momentarily addressing the journalist and her cameraman (_kennats_ as in _(ees) kennats_). _Kennat_ is the [Konjunktiv II](subjunctive-mood.md#-at-inflections) conjugation of _kennen_. It's also possible the 90s microphone did not capture a subtle "n" that would continue the formal Siezen established in his initial question (i.e. _kennatn's_ as in _kennatn Sie_).
