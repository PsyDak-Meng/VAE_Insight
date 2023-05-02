html_layout = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>VAE-Insight</title>
    <link rel="icon" href="../static/favicon.ico">
    <link rel="stylesheet" href="../static/css/base.css">
    <link rel="stylesheet" href="../static/css/main.css">
</head>

<body id="top">

    <div id="preloader">
        <div id="loader" class="dots-fade">
            <div></div>
            <div></div>
            <div></div>
        </div>
    </div>

        <!-- Header
    ================================================== -->
    <header class="s-header">

        <div class="row">

            <div class="s-header__content column">
                <h1 class="s-header__logotext">
                    <a href="../" title="">VAE-Insight</a>
                </h1>
                <p class="s-header__tagline">A Vaccine Adverse Event Prediction System.</p>
            </div>

        </div> <!-- end row -->

        <nav class="s-header__nav-wrap">
            <div class="row">
                <ul class="s-header__nav">
                    <li><a href="../">Home</a></li>
                    <li><a href="../login">Login</a></li>	
                    <li><a href="../prediction">Prediction</a></li>	
                    <li class="current"><a href="../factors">Factors</a></li>
                    <li class="has-children"><a href="#0">Articles</a>
                        <ul>
                            <li><a href="../introduction">Introduction</a></li>
                            <li><a href="../instruction">Instruction</a></li>
                            <li><a href="../referenced">References</a></li>
                        </ul>
                    </li>
                </ul> <!-- end #nav -->
            </div> 
        </nav> <!-- end #nav-wrap -->

    </header> <!-- Header End -->


    <!-- Content
    ================================================== -->

    <div class="s-content">
        <div class="row">

            <div id="main" class="s-content__main large-8 column">
                {%app_entry%}
            </div>



            <div id="sidebar" class="s-content__sidebar large-4 column">
            
                <!-- <div class="widget widget--categories">
                    <h3 class="h6">Adverse Effect.</h3> 
                    <ul>
                        <li><a href="#0" title="">effect 1</a>()</li>
                        <li><a href="#0" title="">effect 2</a>()</li>
                        <li><a href="#0" title="">effect 3</a>()</li>
                    </ul>
                </div> -->
            
                <div class="widget widget_tags">
                    <h3 class="h6">Useful Techniques</h3>
        
                    <div class="tagcloud group">
                        <a href="https://www.sciencedirect.com/science/article/abs/pii/S0020025519308588">Keyword Extraction</a>
                        <a href="https://dash.plotly.com/">Data Visualization</a>
                        <a href="https://en.m.wikipedia.org/wiki/Multilayer_perceptron">Prediction Model</a>
                    </div>
                </div>
            
                <div class="widget widget_popular">
                    <h3 class="h6">References.</h3>
        
                    <ul class="link-list">
                        <li><a href="https://pubmed.ncbi.nlm.nih.gov/34935921/">Analysis of COVID-19 vaccine type and adverse effects following vaccination.</a></li>
                        <!-- <li><a href="https://pubmed.ncbi.nlm.nih.gov/34089044/">Infectious disease mRNA vaccines and a review on epitope prediction for Vaccine Design.</a></li> -->
                        <li><a href="https://www.sciencedirect.com/science/article/abs/pii/S0020025519308588">YAKE! Keyword extraction from single documents using multiple local features.</a></li>
                        <!-- <li><a href="https://pubmed.ncbi.nlm.nih.gov/36399990/">Social Communication Pathways to covid-19 vaccine side-effect expectations and experience.</a></li> -->
                        <li><a href="https://www.nejm.org/doi/full/10.1056/NEJMp1714229">Implementing machine learning in health care - addressing ethical challenges.</a></li>
                        <!-- <li><a href="https://ieeexplore.ieee.org/document/7733254">Automatic Keyword Extraction from Medical and Healthcare Curriculum.</a></li> -->
                        <li><a href="https://pubmed.ncbi.nlm.nih.gov/20045099/">A postmodern Pandora's box: Anti-vaccination misinformation on the Internet.</a></li>
                        <!-- <li><a href="https://pubmed.ncbi.nlm.nih.gov/34607748/">Factors influencing adverse events following immunization with AZD1222 in Vietnamese adults during first half of 2021.</a></li> -->
                        <li><a href="https://pubmed.ncbi.nlm.nih.gov/11257375/">Understanding those who do not understand: a brief review of the anti-vaccine movement.</a></li>
                        <li><a href="https://pubmed.ncbi.nlm.nih.gov/27049120/">Can the vaccine adverse event reporting system be used to increase vaccine acceptance and trust?</a></li>
                        <!-- <li><a href="https://pubmed.ncbi.nlm.nih.gov/28284680/">Psychological factors associated with uptake of the childhood influenza vaccine and perception of post-vaccination side-effects: A cross-sectional survey in England.</a></li> -->
                        <li><a href="https://pubmed.ncbi.nlm.nih.gov/26209838/">Safety monitoring in the Vaccine Adverse Event Reporting System (VAERS).</a></li>
                        <!-- <li><a href="https://ieeexplore.ieee.org/document/9971547">Key information extraction method of traditional Chinese medicine records based on TF-IDF and K-means.</a></li> -->
                    </ul>
                </div>

            </div> <!-- end sidebar -->
        </div> <!-- end row -->    

    </div> <!-- end content-wrap -->


    {%config%}
    {%scripts%}
    {%renderer%}

    <!-- Footer
    ================================================== -->
    <footer class="s-footer">

        <div class="row s-footer__bottom">

            <div class="large-6 tab-full column s-footer__info">
                <h3 class="h6">About VAE-Insight</h3>

                <p>
                    The VAE-Insight is design to make some difference in helping every person who may not understand those obscure biomedical sciences figure out the effects of the vaccine, 
            especially its harmful effects, considering that its positivity has been well reported and publicized.
                </p>

                <p>
                    The VAE-Insight is an integrated system including user-friendly web interface, 
                    user-data management, adverse effect prediction, and data visualization.
                </p>
            </div>

            <div class="large-6 tab-full column">
                <div class="row">
                    <div class="large-5 tab-full column">

                        <h3 class="h6">Photostream</h3>
                        
                        <ul class="photostream group">
                            <li><a href="#0"><img alt="thumbnail" src="../static/images/photo/1.png"></a></li>
                            <li><a href="#0"><img alt="thumbnail" src="../static/images/photo/2.png"></a></li>
                            <li><a href="#0"><img alt="thumbnail" src="../static/images/photo/3.png"></a></li>
                            <li><a href="#0"><img alt="thumbnail" src="../static/images/photo/4.png"></a></li>
                            <li><a href="#0"><img alt="thumbnail" src="../static/images/photo/5.png"></a></li>
                        </ul>
        
                    </div>
        
                    <div class="large-4 tab-full column">
                        <h3  class="h6">Navigate</h3>
        
                        <ul class="s-footer__list s-footer-list--nav group">
                            <li><a href="{{ url_for('index') }}">Home</a></li>
                            <li><a href="{{ url_for('login') }}">Login</a></li>	
                            <li><a href="{{ url_for('prediction') }}">Prediction</a></li>	
                            <li><a href="{{ url_for('factors') }}">Factors</a></li>
                        </ul>
                    </div>
                </div>
            </div>

            <div class="ss-copyright">
                <span>© Copyright VAE-Insight 2023</span> 
                <span>Design by - TEAM023</a></span>
                <span><a href="https://www.styleshout.com">Credit Link</a></span>
            </div>


        <div class="ss-go-top">
            <a class="smoothscroll" title="Back to Top" href="#top">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path d="M12 0l8 9h-6v15h-4v-15h-6z"/></svg>
            </a>
        </div> <!-- end ss-go-top -->

    </footer> <!-- end Footer-->

    <!-- Java Script
    ================================================== -->
    <script src="../static/js/jquery-3.2.1.min.js"></script>
    <script src="../static/js/main.js"></script>

</body>
</html>


"""