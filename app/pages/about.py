import streamlit as st
from components.navbar import render_navbar
from utils.image_loader import load_image_base64
from utils.path_helper import get_asset_path


def about():
    render_navbar(current_page="about")

    #about section
    st.markdown(
        """
            <div class='about-section'>
                <div class='about-title'>About PredictMyPay</div>
                <div class='about-description'>
                    A modern data-driven web application that leverages machine learning to provide accurate salary predictions based on comprehensive data analysis.
                </div>
            </div>
        """, unsafe_allow_html=True
    )

    #about section styles
    st.markdown(
        """
            <style>
                .about-section {
                    max-width: 75vw;
                    min-width: 75vw;
                    padding: 3rem 2rem;
                    background-color: #f8faf4;
                    border-radius: 20px;
                    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.05);
                    text-align: center;
                    margin: 1rem auto 0rem;
                }

                .about-title {
                    font-size: 3.3rem;
                    font-weight: 600;
                    margin-bottom: 1rem;
                    color: #222;
                }

                .about-description {
                    font-size: 1.2rem;
                    font-weight: 600;
                    color: #555;
                    line-height: 1.6;
                    max-width: 800px;
                    margin: 0 auto;
                }
            </style>
        """, unsafe_allow_html=True
    )

    # project overview section
    project_overview_image_path = get_asset_path("project-overview.png")
    project_overview_icon_src = load_image_base64(project_overview_image_path)

    #project overview section html
    project_overview_html = f"""
    <div class='project-overview-section'>
    <div class='project-overview-title'>
        <img src='{project_overview_icon_src}' width='50' height='50' style='margin-right:10px;'/>
        <h1>Project Overview</h1>
    </div>

    <div class='overview-description'>
    PredictMyPay is an innovative web application designed to democratize salary information through data-driven insights.
    Our platform utilizes advanced machine learning algorithms to analyze vast datasets and provide accurate salary predictions
    based on various factors including experience, location, industry, and skills.
    <br><br>
    Built with a commitment to transparency and fairness, PredictMyPay helps job seekers, employers, and career professionals
    make informed decisions about compensation expectations and market trends.
    </div>
    </div>
    """
    st.markdown(project_overview_html, unsafe_allow_html=True)

    #project overview section styles
    st.markdown(
        """
            <style>
                .project-overview-section {
                    max-width: 75vw;
                    min-width: 75vw;
                    background-color: #f7f9fa;
                    padding: 2rem;
                    border-radius: 16px;
                    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
                    margin: 2rem auto 0;
                }

                .project-overview-title{
                    display: flex;
                    justify-content: center;
                    align-items: center;    
                }
                
                .project-overview-title h1{
                    text-align: center;
                    font-size: 2rem;
                    font-weight: 600;
                    color: #222;
                }

                .overview-description {
                    font-size: 1.2rem;
                    font-weight: 600;
                    color: #555;
                    line-height: 1.6;
                    max-width: 850px;
                    margin: 0 auto;
                }

                .overview-img {
                    max-width: 100%;
                    display: block;
                    margin: 0 auto 1.5rem auto;
                    border-radius: 12px;
                    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
                }        
            </style>
        """, unsafe_allow_html=True
    )


    #how it works section
    working_image_path = get_asset_path("working.png")
    working_icon_src = load_image_base64(working_image_path)

    data_image_path = get_asset_path("database.png")
    data_icon_src = load_image_base64(data_image_path)

    ml_processing_image_path = get_asset_path("ml-processing.png")
    ml_processing_icon_src = load_image_base64(ml_processing_image_path)

    prediction_image_path = get_asset_path("prediction.png")
    prediction_icon_src = load_image_base64(prediction_image_path)
    
    working_html = f"""
    <div class='working-section'>

    <!-- Title with icon on left, centered -->
    <div class='working-title'>
    <img src='{working_icon_src}' class='title-icon'/>
    <div class='title-text'>How It Works</div>
    </div>

    <!-- Steps container -->
    <div class='working-steps'>

    <div class='step'>
    <div class='step-icon' style='background-color: #ebf2f2;'>
        <img src='{data_icon_src}' width='40' height='40'/>
    </div>
    <div class='step-title'>Data Collection</div>
    <p>Comprehensive salary data from multiple reliable sources</p>
    </div>

    <div class='step'>
    <div class='step-icon' style='background-color: #fef6eb;'>
        <img src='{ml_processing_icon_src}' width='40' height='40'/>
    </div>
    <div class='step-title'>ML Processing</div>
    <p>XGBoost algorithms analyze patterns and relationships</p>
    </div>

    <div class='step'>
    <div class='step-icon' style='background-color: #ebf2f2;'>
        <img src='{prediction_icon_src}' width='40' height='40'/>
    </div>
    <div class='step-title'>Prediction</div>
    <p>Accurate salary estimates with confidence intervals</p>
    </div>

    </div>

    </div>
    """
    st.markdown(working_html, unsafe_allow_html=True)

    #working section styles
    st.markdown(
    """
    <style>
        .working-section {
            background-color: white;
            max-width: 75vw;
            min-width: 75vw;
            margin: 2rem auto 0;
            padding: 2rem;
            border-radius: 20px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.05);
        }

        .working-title {
            display: flex;
            justify-content: center;
            align-items: center;
            margin-bottom: 2rem;
        }

        .title-icon {
            width: 50px;
            height: 50px;
            margin-right: 10px;
        }

        .title-text {
            font-size: 2rem !important;
            font-weight: 600 !important;
            margin: 0;
        }

        .working-steps {
            display: flex;
            justify-content: space-around;
            flex-wrap: wrap;
            gap: 2rem;
        }

        .step {
            display: flex;
            flex-direction: column;
            justify-content: space-around;
            align-items: center;
            max-width: 350px;
            text-align: center;
        }

        .step-icon {
            width: 100%;
            padding: 1rem;
            border-radius: 1rem;
            margin-bottom: 1rem;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .step-title {
            font-size: 1.5rem;
            font-weight: 600;
        }

        .step p {
            font-size: 1rem;
            font-weight: 600;
            color: #555;
            line-height: 1.6;
        }
    </style>
    """, unsafe_allow_html=True
    )


    #technologies used section
    technology_image_path = get_asset_path("technology-title-icon.png")
    technology_icon_src = load_image_base64(technology_image_path)

    python_image_path = get_asset_path("python.png")
    python_icon_src = load_image_base64(python_image_path)

    streamlit_image_path = get_asset_path("streamlit.png")
    streamlit_icon_src = load_image_base64(streamlit_image_path)

    xgboost_image_path = get_asset_path("xg-boost.png")
    xgboost_icon_src = load_image_base64(xgboost_image_path)

    pandas_image_path = get_asset_path("pandas.png")
    pandas_icon_src = load_image_base64(pandas_image_path)

    technologies_html = f"""
    <div class='technologies-section'>

    <!-- Title with icon on left, centered -->
    <div class='technologies-title'>
    <img src='{technology_icon_src}' class='title-icon'/>
    <div class='title-text'>Technologies Used</div>
    </div>

    <!-- Tech grid container -->
    <div class='technologies-grid'>

    <div class='tech-card'>
    <div class='tech-icon' style='background-color: #f0f7ff;'>
        <img src='{python_icon_src}' width='40' height='40'/>
    </div>
    <div class='tech-title'>Python</div>
    <p>Core Language</p>
    </div>

    <div class='tech-card'>
    <div class='tech-icon' style='background-color: #fef6eb;'>
        <img src='{streamlit_icon_src}' width='40' height='40'/>
    </div>
    <div class='tech-title'>Streamlit</div>
    <p>Web Framework</p>
    </div>

    <div class='tech-card'>
    <div class='tech-icon' style='background-color: #f0f5f4;'>
        <img src='{xgboost_icon_src}' width='40' height='40'/>
    </div>
    <div class='tech-title'>XGBoost</div>
    <p>ML Algorithm</p>
    </div>

    <div class='tech-card'>
    <div class='tech-icon' style='background-color: #fff5f7;'>
        <img src='{pandas_icon_src}' width='40' height='40'/>
    </div>
    <div class='tech-title'>Pandas</div>
    <p>Data Analysis</p>
    </div>

    </div>

    </div>
    """
    st.markdown(technologies_html, unsafe_allow_html=True)


    #technologies used section style
    st.markdown(
    """
    <style>
        .technologies-section {
            background-color: white;
            max-width: 75vw;
            min-width: 75vw;
            margin: 2rem auto 0;
            padding: 2rem;
            border-radius: 20px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.05);
        }

        .technologies-title {
            display: flex;
            justify-content: center;
            align-items: center;
            margin-bottom: 2rem;
        }

        .title-icon {
            width: 50px;
            height: 50px;
            margin-right: 10px;
        }

        .title-text {
            font-size: 2rem !important;
            font-weight: 600 !important;
            margin: 0;
        }

        .technologies-grid {
            display: flex;
            justify-content: space-around;
            flex-wrap: wrap;
            gap: 2rem;
        }

        .tech-card {
            display: flex;
            flex-direction: column;
            justify-content: space-around;
            align-items: center;
            margin: auto;
            max-width: 250px;
            text-align: center;
        }

        .tech-icon {
            width: 100%;
            padding: 1rem;
            border-radius: 1rem;
            margin-bottom: 1rem;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .tech-title {
            font-size: 1.25rem;
            font-weight: 600;
        }

        .tech-card p {
            font-size: 1rem;
            font-weight: 500;
            color: #555;
            line-height: 1.5;
        }
        </style>
    """, unsafe_allow_html=True)

    #about creator section
    about_creator_img_path = get_asset_path('user.png')
    about_creator_icon_src = load_image_base64(about_creator_img_path)

    creator_img_path = get_asset_path('creator.png')
    creator_img_src = load_image_base64(creator_img_path)

    linkedin_img_path = get_asset_path('linkedin.png')
    linked_icon_src = load_image_base64(linkedin_img_path)

    github_img_path = get_asset_path('github.png')
    github_icon_src = load_image_base64(github_img_path)

    about_creator_html = f"""
    <div class="about-creator-section">
    <div class="about-creator-title">
    <img src="{about_creator_icon_src}" width="30" style="margin-right:10px;" />
    <div class="about-creator-title-text">About the Creator</div>
    </div>

    <div class="about-creator-content">
    <div class="creator-image">
    <img src="{creator_img_src}" alt="Creator Image" />
    </div>
    <div class="creator-details">
    <div class="creator-details-title">Data Scientist and Developer</div>
    <p class="creator-bio">
    Passionate about leveraging data science and machine learning to solve real-world problems.
    With expertise in Python, machine learning algorithms, and web development, I created
    <strong>PredictMyPay</strong> to bridge the gap between complex data analytics and practical salary insights.
    </p>

    <div class="creator-links">
    <a href="https://www.linkedin.com/in/sulav-man-sing-tamang-269bb5190/" target="_blank" class="link-icon linkedin">
    <img src="{linked_icon_src}" />
    <span>LinkedIn</span>
    </a>

    <a href="https://github.com/sulavtamang" target="_blank" class="link-icon github">
    <img src="{github_icon_src}" />
    <span>GitHub</span>
    </a>
    </div>
    </div>
    </div>
    </div>
    """
    st.markdown(about_creator_html, unsafe_allow_html=True)

    #about creator section styles
    st.markdown("""
    <style>
    .about-creator-section {
        max-width: 75vw;
        min-width: 74vw;
        margin: 2rem auto 0;
    }

    .about-creator-title {
        display: flex;
        align-items: center;
        margin-bottom: 1.5rem;
    }

    .about-creator-title-text {
        font-size: 2rem;
        font-weight: 600;
        margin: 0;
    }

    .about-creator-content {
        display: flex;
        justify-content; center;
        align-items: center;
        flex-wrap: wrap;        
        gap: 2rem;
    }

    .creator-image img {
        background-color: #e4e5e4;
        width: 180px;
        height: 180px;
        border-radius: 50%;
        object-fit: cover;
        box-shadow: 0 0 10px rgba(0,0,0,0.1);
    }

    .creator-details {
        flex: 1;
        min-width: 250px;
    }

    .creator-details-title {
        margin-top: 0;
        font-size: 1.4rem;
        font-weight: 600;
        color: #333;
    }

    .creator-bio {
        font-size: 1rem;
        font-weight: 600;
        color: #555;
        margin-top: 0.5rem;
        margin-bottom: 1rem;
        line-height: 1.6;
    }

    .creator-links {
        display: flex;
        flex-wrap: wrap;
        gap: 1.5rem;
    }
                
    .creator-links a{
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: 0.9rem;
        padding: 1rem 2rem;
        text-decoration: none;
        color: white;
    }

   .link-icon {
        display: flex;
        align-items: center;
        gap: 0.5rem;
        text-decoration: none;
        color: #333;
        font-weight: 500;
        border-radius: 0.5rem;
        padding: 0.6rem 1rem;
        transition: transform 0.2s ease, box-shadow 0.3s ease;
    }

    .link-icon img {
        width: 20px;
        height: 20px;
    }

    .link-icon.linkedin {
        background-color: #377e7f;
    }

    .link-icon.github {
        background-color: #212936;
    }

    .link-icon:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        /* Text color remains unchanged */
    }


    .link-icon img {
        width: 30px;
        height: 30px;
    }
    </style>
    """, unsafe_allow_html=True)


    #footer section
    st.markdown("""
        <div class="footer">
            <div class='footer-title'>PredictMyPay</div>
            <div class='footer-subtitle'>Empowering career decisions through data-driven salary insights</div>
            <div class='footer-bottom'>© 2024 PredictMyPay. All rights reserved.</div>
        </div>
    """, unsafe_allow_html=True)

    # footer styles
    st.markdown("""
        <style>
            .footer {
                max-width: 75vw;
                margin: 2rem auto 0rem;
                padding: 2rem 1rem;
                background-color: #f8f9fa;
                text-align: center;
                color: #444;
                border-top: 1px solid #e0e0e0;
                font-family: 'Poppins', sans-serif;
            }

            .footer-title {
                padding: 0;
                margin: 0;
                font-size: 1.4rem;
                font-weight: 600;
                color: #d4583a;
            }

            .footer-subtitle {
                padding: 0;
                margin: 0;
                font-size: 1rem;
                font-weight: 600;
                color: #555;
            }

            .footer-bottom {
                display: block;
                margin-top: 1rem;
                font-size: 0.9rem;
                color: #888;
            }
        </style>
    """, unsafe_allow_html=True)


    # media query styles 
    st.markdown("""
        <style>
            /* For large tablets & small desktops */
            @media (max-width: 992px) {
                .about-section,
                .project-overview-section,
                .working-section,
                .technologies-section,
                .about-creator-section,
                .footer {
                    max-width: 90vw !important;
                    min-width: auto !important;
                    padding: 1.8rem !important;
                    margin: 1rem auto !important;
                    border-radius: 14px !important;
                    box-shadow: 0 3px 8px rgba(0, 0, 0, 0.08) !important;
                }
            }

            /* For tablets & large phones */
            @media (max-width: 768px) {
                .about-section,
                .project-overview-section,
                .working-section,
                .technologies-section,
                .about-creator-section,
                .footer {
                    max-width: 95vw !important;
                    min-width: auto !important;
                    padding: 1.5rem !important;
                    margin: 1rem auto !important;
                    border-radius: 12px !important;
                    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.06) !important;
                }

                .about-title {
                    font-size: 2.4rem !important;
                }

                .project-overview-title h1,
                .working-title .title-text,
                .technologies-title .title-text,
                .about-creator-title-text {
                    font-size: 1.6rem !important;
                }

                .step-title {
                    font-size: 1.2rem !important;
                }
                .about-creator-content{
                    flex-direction: column;
                }
            }

            /* For small phones */
            @media (max-width: 480px) {
                .about-section,
                .project-overview-section,
                .working-section,
                .technologies-section,
                .about-creator-section,
                .footer {
                    max-width: 100vw !important;
                    min-width: auto !important;
                    padding: 1rem !important;
                    margin: 0.8rem auto !important;
                    border-radius: 8px !important;
                    box-shadow: 0 1px 4px rgba(0, 0, 0, 0.05) !important;
                }

                .about-title {
                    font-size: 1.8rem !important;
                }
                .about-description,
                .overview-description,
                .step p,
                .tech-card p,
                .creator-bio,
                .footer-subtitle{
                    font-size: 0.8rem !important;
                }

                .project-overview-title h1,
                .working-title .title-text,
                .technologies-title .title-text,
                .about-creator-title-text {
                    font-size: 1.2rem !important;
                }

                .step-title {
                    font-size: 1rem !important;
                }

                .creator-image img {
                    width: 130px !important;
                    height: 130px !important;
                }

                .creator-details {
                    min-width: auto !important;
                }

                .technologies-grid {
                    flex-direction: column !important;
                    gap: 1rem !important;
                }

                .working-steps {
                    flex-direction: column !important;
                    gap: 1rem !important;
                }
            }
        </style>
    """, unsafe_allow_html=True)
