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

span[lang="at"] {
    display: none;
}

span[lang="de"] {
    display: none;
    font-size: .83em;
    /* line-height: 0.5em; */
    vertical-align: baseline;
    position: relative;
    top: -0.4em;
}
</style>

<script>
function revealSelector(window, selector) {
    var window_element = document.querySelector(window);
    var list = window_element.querySelectorAll(selector);
    for (var i=0, element; element = list[i]; i++) {
        element.style.display="inline";
        element.style.backgroundColor="inherit";
        element.style.color="inherit";
    }
}

function iterButton(window, button) {
    if (!button.getAttribute("state")) {
        revealSelector(window, 'span[lang="at"]');
        button.innerHTML = 'Show <img alt="🇩🇪" class="twemoji" src="https://cdn.jsdelivr.net/gh/jdecked/twemoji@15.0.3/assets/svg/1f1e9-1f1ea.svg" title="Standard German"> subtitles';
        button.setAttribute("state", "1");
    } else if (button.getAttribute("state") === "1") {
        revealSelector(window, 'span[lang="de"]');
        button.textContent = 'Show spoilers';
        button.setAttribute("state", "2");
    } else if (button.getAttribute("state") === "2") {
        revealSelector(window, '.spoiler');
        button.textContent = 'Done';
        button.setAttribute("state", "3");
    }
}
</script>

## Mundl

![type:video](https://www.youtube.com/embed/rgib5xy8MJ4?fs=0&playsinline=1&rel=0&start=54&end=63){ referrerpolicy="strict-origin-when-cross-origin" }

<button class="md-button" onclick="iterButton('#mundl-subs', this)">Show {{at}} subtitles</button>

<div id="mundl-subs" markdown="1">

> |at|> :factory_worker: Prost, Oida.  
> |de|> Prost, Alter.  
> |at|> :man_bald_tone1: Du sogst olle "Oida" zu mia, !!heast!!. Haaß Mundl.  
> |de|> Du sagst alle "Alter" zu mir, hörst du. Ich heiße Mundl.  
> |at|> :factory_worker: Servas.  
> |de|> Servus.  

</div>

## Schoafe Schoaf

![type:video](https://www.youtube.com/embed/B2X0NUJhT-4?fs=0&playsinline=1&rel=0&start=35&end=62){ referrerpolicy="strict-origin-when-cross-origin" }

<button class="md-button" onclick="iterButton('#mustache-subs', this)">Show {{at}} subtitles</button>

<!-- why markdown="1"? https://stackoverflow.com/questions/47165449/use-static-html-in-mkdocs -->
<div class="annotate" id="mustache-subs" markdown="1">

> |at|> :man_tone1: Schoafe Schoaf. Danke.  
> |de|> Scharfe Scharf. Danke.  
> |at|> :woman: !!Sog!!, wos is a schoafe Schoaf?  
> |de|> Sag, was ist eine "scharfe Scharf?"  
> |at|> :man_tone1: Sie !!san!! von Wien? :woman: _Ja._  
> |de|> Sie sind von Wien? _Ja._  
> |at|> :man_tone1: Warum !!kennat's!! des ned? (1)  
> |de|> Warum kennte sie das nicht?  
> |at|> :man_tone1: Schoafe Schoaf is a schoafe Burnwurst mid schoafm Senf. Schoaf, Schoaf.  
> |de|> "Scharfe Scharf" ist eine scharfe Burenwurst mit scharfem Senf. Scharf, Scharf.  
> |at|> :man_tone1: Also, !!brauch!! ma ned mehrere Sochn.  
> |de|> Also, braucht man nicht mehrere Sachen.  
> |at|> :man_tone1: !!Song!! so, muss aanfoch "schoaf Schoaf."  
> |de|> Sagen so, (es) muss einfach "scharf Scharf."  
> |at|> :man_tone1: "Schoafe Schoaf" is schoafe Schoaf.  
> |de|> "Scharfe Scharf" ist "scharfe Scharf."  
> |at|> :man_tone1: Es is, is irgendwo verständlich, oder hob mi -- hob i mi richtig !!aufgregt!!.  
> |de|> Es ist, ist irgendwo verständlich, oder habe mich -- habe ich mich richtig aufgeregt.  

</div>

1. The man is either speaking aside to himself for a moment (_kennat's_ as in _kennat se_) or momentarily addressing the journalist and her cameraman (_kennats_ as in _(ees) kennats_). _Kennat_ is the [Konjunktiv II](subjunctive-mood.md#-at-inflections) conjugation of _kennen_. It's also possible the 90s microphone did not capture a subtle "n" that would continue the formal Siezen established in his initial question (i.e. _kennatn's_ as in _kennatn Sie_).

## Brigitta vom Gemüsestand

<!-- https://www.youtube.com/watch?v=xFaKeo_isPo -->
![type:video](https://www.youtube.com/embed/xFaKeo_isPo?fs=0&playsinline=1&rel=0&start=0&end=5){ referrerpolicy="strict-origin-when-cross-origin" }

<button class="md-button" onclick="iterButton('#brigitta-subs', this)">Show {{at}} subtitles</button>

<div class="annotate" id="brigitta-subs" markdown="1">

> |at|> :older_woman_tone1: Frische Karotten. Olles Frisch heite. Kommts (1) her, meine Hausfraun.  
> |de|> Frische Karotten. Alles Frisch heute. Kommt ihr her, meine Hausfrauen.  

</div>

1. "Kommts" is the [conjugation of Kommen in the 2PL](present-tense.md)

> |at|> :older_woman_tone1: Frische Karotten. Olles Frisch heite. Kommts her, meine Hausfraun.
> |de|> Frische Karotten. Alles Frisch heute. Kommt ihr her, meine Hausfrauen.
