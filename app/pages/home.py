import streamlit as st
from streamlit_javascript import st_javascript
from components.navbar import render_navbar

def home():
    render_navbar(current_page='home')

    # Hero section
    st.markdown("""
        <div class="hero-container">
            <div class="hero-title">PredictMyPay</div>
            <div class="hero-subtitle">
                <span class="highlight">Wondering what salary you truly deserve?</span><br />
                <span class="accent">PredictMyPay</span> uses <span class="highlight">data science</span> and 
                <span class="highlight">machine learning</span> to offer <span class="accent">personalized salary insights</span> 
                tailored to your <span class="highlight">skills, experience,</span> and <span class="highlight">job role</span>.<br />
                Take the <span class="accent">guesswork</span> out of career planning — know your worth with confidence.
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # CSS for hero section 
    st.markdown("""
        <style>
            .hero-container {
                display: flex;
                flex-direction: column;
                justify-content: center;
                gap: 1rem;
                align-items: center;
                height: 40vh;
                padding: 2rem 1rem 1rem;
                text-align: center;
                background-color: #f7f9fc;
            }

            /* MAIN TITLE */
            .hero-title {
                font-size: clamp(2rem, 5vw, 3rem); /* Smooth scale */
                font-weight: 800;
                color: #008080;
            }

            /* SUBTITLE */
            .hero-subtitle {
                font-size: clamp(1rem, 2.5vw, 1.3rem); /* Scales with screen size */
                font-weight: 500;
                color: #333;
                max-width: 750px;
                line-height: 1.6;
            }

            /* HIGHLIGHTED KEYWORDS */
            .highlight {
                color: #FF8C00;
                font-weight: 600;
            }

            /* ACCENT PHRASES */
            .accent {
                color: #008080;
                font-style: italic;
                font-weight: 500;
            }

            /* EXTRA SMALL SCREENS (like small phones) */
            @media (max-width: 480px) {
                .hero-title {
                    font-size: 1.8rem;
                    font-weight: 700;
                }
                .hero-subtitle {
                    font-size: 0.9rem;
                    font-weight: 400;
                }
            }

            /* ULTRA SMALL SCREENS (older phones or very narrow views) */
            @media (max-width: 350px) {
                .hero-title {
                    font-size: 1.6rem;
                    font-weight: 600;
                }
                .hero-subtitle {
                    font-size: 0.75rem;
                    font-weight: 400;
                }
            }
        </style>
    """, unsafe_allow_html=True)


    # Use HTML-based CTA button with the matching class
    st.markdown(
        """
        <a class="cta_home" href="/?page=predict" target="_self">
            <button>🚀 Start Predicting Now!</button>
        </a>
        """,
        unsafe_allow_html=True
    )

    #cta button style
    st.markdown("""
        <style>
        a.cta_home {
            text-decoration: none;
        }
                
        a.cta_home button{
            background-color: #DC143C;
            color: #FFF8DC;
            font-size: clamp(16px, 2vw, 24px);
            font-weight: bold;
            border-radius: 10px;
            padding: 12px 28px;
            border: none;
            box-shadow: 0 4px 12px rgba(220, 20, 60, 0.5);
            transition: all 0.3s ease;
            white-space: nowrap;
            width: 100%;
            max-width: 360px;
            margin: auto;
            display: block;
            cursor: pointer;
        }

        a.cta_home button:hover {
            background-color: #FF4500;
            color: #FFFFFF;
            transform: scale(1.08);
            box-shadow: 0 6px 16px rgba(255, 69, 0, 0.7);
        }
                
        @media (max-width: 480px) {
            a.cta_home button {
                font-size: 16px;
                font-weight: 600;
            }
        }

        @media (min-width: 481px) and (max-width: 768px) {
            a.cta_home button {
                font-size: 18px;
                font-weight: 600;
            }
        }

        @media (min-width: 769px) and (max-width: 1024px) {
            a.cta_home button {
                font-size: 20px;
                font-weight: 700;
            }
        }

        @media (min-width: 1025px) {
            a.cta_home button {
                font-size: 22px;
                font-weight: 700;
            }
        }
        </style>
    """, unsafe_allow_html=True)


