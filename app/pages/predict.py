import streamlit as st
from components.navbar import render_navbar
from utils.model import predict_salary

def predict():
    render_navbar(current_page='predict')

    # css for form
    st.markdown("""
        <style>
            body {
                background: linear-gradient(to bottom right, #f8f9fc, #e4ecf7);
            }

            .form-header {
                max-width: 600px;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                margin: auto;
                padding: 1rem 3rem;
            }
            .form-header-title {
                font-size: 2rem;
                font-weight: 700;
                color: #2f4b7c;
                margin-bottom: 0.5rem;
                text-align: center;
            }

            .form-header-subtitle {
                font-size: 1.1rem;
                font-weight: 400;
                color: #555e7b;
                text-align: center;
                display: block;
            }

            .stForm {
                max-width: 600px;
                min-width: 45vw;
                margin: 0 auto;
                padding: 2rem;
            }

            label {
                color: #374151 !important;
                font-weight: 600;
                fo`nt-size: 1rem;
            }

            input, select, textarea {
                background-color: #f1f5f9 !important;
                border: 1px solid #d1d5db !important;
                font-size: 1rem;
                color: #111827 !important;
                border-radius: 6px !important;

                box-shadow: none !important;
                padding: 0.5rem !important;
                width: 100% !important;
                caret-color: black !important; /* show blinking cursor */
            }

            .stNumberInput input {
                background-color: #f9f9f9 !important;
                border: none !important;
                box-shadow: none !important;
                border-radius: 0px !important;
                padding: 0.5rem !important;
                width: 100% !important;
                color: black !important;
                caret-color: black !important;
            }

            input::placeholder {
                color: #9ca3af !important;
            }

            /* Fix number spinner buttons background */
            input[type="number"]::-webkit-inner-spin-button {
                background: #f9f9f9 !important;
            }

            button[kind="secondaryFormSubmit"] {
                background: linear-gradient(to right, #f97316, #fb923c) !important;
                color: white !important;
                border-radius: 8px !important;
                box-shadow: 0 4px 12px rgba(249, 115, 22, 0.3);
                font-weight: 700;
                font-size: 16px;
                transition: background 0.3s ease;
            }
                
            button[kind="secondaryFormSubmit"]:hover {
                background: linear-gradient(to right, #ea580c, #f59e0b) !important;
            }

            /* Style number input buttons (+ / -) */
            button[data-testid="stNumberInputStepUp"],
            button[data-testid="stNumberInputStepDown"] {
                background-color: #f9f9f9 !important;
                border: none !important;
                color: #333 !important;
                padding: 0.5rem;
                border-radius: 0px !important;
                transition: background-color 0.2s ease;
            }

            button[data-testid="stNumberInputStepUp"]:hover,
            button[data-testid="stNumberInputStepDown"]:hover {
                background-color: #eaeaea !important;
            }
                
            /* Style the outer select box */
            div[data-baseweb="select"] {
                background-color: #f9f9f9 !important;
                border: none !important;
                border-radius: 0px !important;
                box-shadow: none !important;
            }

            /* Style the inner value display */
            div[data-baseweb="select"] > div {
                background-color: #f9f9f9 !important;
                color: #000 !important;
                font-weight: 500;
            }

            /* Optional: Style the input inside the select dropdown */
            div[data-baseweb="select"] input {
                background-color: #f9f9f9 !important;
                color: #000 !important;
                border: none !important;
            }
                
            div[data-baseweb="base-input"] {
                background-color: #f9f9f9 !important;
                border: none !important;
                border-radius: 0px !important;
                box-shadow: none !important;
            }
                
            /* Fix browser autofill background color */
            input:-webkit-autofill {
                -webkit-box-shadow: 0 0 0px 1000px #f9f9f9 inset !important;
                -webkit-text-fill-color: #000 !important;
                caret-color: #000 !important;
            }
                
            .stAlertContainer {
                background-color: darkred;
            }

            /* Medium Screens (Tablet) */
            @media (max-width: 900px) {
                .form-header-title {
                    font-size: 1.8rem;
                    font-weight: 700;
                }

                .form-header-subtitle {
                    font-size: 1rem;
                    font-weight: 400;
                }

                label {
                    font-size: 0.95rem;
                    font-weight: 600;
                }

                input, select, textarea {
                    font-size: 1rem;
                }

                button[kind="secondaryFormSubmit"] {
                    font-size: 15px;
                    font-weight: 700;
                }
            }

            /* Small Screens (Mobile) */
            @media (max-width: 600px) {
                .form-header-title{
                    font-size: 1.5rem;
                    font-weight: 700;
                }

                .form-header-subtitle {
                    font-size: 0.9rem;
                    font-weight: 400;
                }

                label {
                    font-size: 0.9rem;
                    font-weight: 600;
                }

                input, select, textarea {
                    font-size: 0.95rem;
                }

                button[kind="secondaryFormSubmit"] {
                    font-size: 14px;
                    font-weight: 700;
                }
            }

            /* Extra Small Screens */
            @media (max-width: 400px) {
                .form-header-title {
                    font-size: 1.2rem;
                }

                .form-header-subtitle{
                    font-size: 0.8rem;
                }

                label, input, select, textarea {
                    font-size: 0.85rem;
                }

                button[kind="secondaryFormSubmit"] {
                    font-size: 13px;
                }
            }
                
            div[style*="background-color: #ecfdf5"] {
                animation: fadeIn 0.6s ease-in-out;
            }

            @keyframes fadeIn {
                from { opacity: 0; transform: translateY(10px); }
                to { opacity: 1; transform: translateY(0); }
            }
        </style>
    """, unsafe_allow_html=True)

    #form container html
    st.markdown("""
            <div class='form-header'>
                <div class='form-header-title'>Predict Your Salary</div>
                <div class='form-header-subtitle'>Get a salary prediction based on your skill and experience. This estimate is based on data from thousands of real job offers. </div>
            </div>
    """, unsafe_allow_html=True)

    job_titles_list = [
    'Software Engineer', 'Data Analyst', 'Senior Manager',
    'Sales Associate', 'Director', 'Marketing Analyst',
    'Product Manager', 'Sales Manager', 'Marketing Coordinator',
    'Senior Scientist', 'Software Developer', 'HR Manager',
    'Financial Analyst', 'Project Manager', 'Customer Service Rep',
    'Operations Manager', 'Marketing Manager', 'Senior Engineer',
    'Data Entry Clerk', 'Sales Director', 'Business Analyst',
    'VP of Operations', 'IT Support', 'Recruiter', 'Financial Manager',
    'Social Media Specialist', 'Software Manager', 'Junior Developer',
    'Senior Consultant', 'Product Designer', 'CEO', 'Accountant',
    'Data Scientist', 'Marketing Specialist', 'Technical Writer',
    'HR Generalist', 'Project Engineer', 'Customer Success Rep',
    'Sales Executive', 'UX Designer', 'Operations Director',
    'Network Engineer', 'Administrative Assistant',
    'Strategy Consultant', 'Copywriter', 'Account Manager',
    'Director of Marketing', 'Help Desk Analyst',
    'Customer Service Manager', 'Business Intelligence Analyst',
    'Event Coordinator', 'VP of Finance', 'Graphic Designer',
    'UX Researcher', 'Social Media Manager', 'Director of Operations',
    'Senior Data Scientist', 'Junior Accountant',
    'Digital Marketing Manager', 'IT Manager',
    'Customer Service Representative', 'Business Development Manager',
    'Senior Financial Analyst', 'Web Developer', 'Research Director',
    'Technical Support Specialist', 'Creative Director',
    'Senior Software Engineer', 'Human Resources Director',
    'Content Marketing Manager', 'Technical Recruiter',
    'Sales Representative', 'Chief Technology Officer',
    'Junior Designer', 'Financial Advisor', 'Junior Account Manager',
    'Senior Project Manager', 'Principal Scientist',
    'Supply Chain Manager', 'Senior Marketing Manager',
    'Training Specialist', 'Research Scientist',
    'Junior Software Developer', 'Public Relations Manager',
    'Operations Analyst', 'Product Marketing Manager',
    'Senior HR Manager', 'Junior Web Developer',
    'Senior Project Coordinator', 'Chief Data Officer',
    'Digital Content Producer', 'IT Support Specialist',
    'Senior Marketing Analyst', 'Customer Success Manager',
    'Senior Graphic Designer', 'Software Project Manager',
    'Supply Chain Analyst', 'Senior Business Analyst',
    'Junior Marketing Analyst', 'Office Manager', 'Principal Engineer',
    'Junior HR Generalist', 'Senior Product Manager',
    'Junior Operations Analyst', 'Senior HR Generalist',
    'Sales Operations Manager', 'Senior Software Developer',
    'Junior Web Designer', 'Senior Training Specialist',
    'Senior Research Scientist', 'Junior Sales Representative',
    'Junior Marketing Manager', 'Junior Data Analyst',
    'Senior Product Marketing Manager', 'Junior Business Analyst',
    'Senior Sales Manager', 'Junior Marketing Specialist',
    'Junior Project Manager', 'Senior Accountant', 'Director of Sales',
    'Junior Recruiter', 'Senior Business Development Manager',
    'Senior Product Designer', 'Junior Customer Support Specialist',
    'Senior IT Support Specialist', 'Junior Financial Analyst',
    'Senior Operations Manager', 'Director of Human Resources',
    'Junior Software Engineer', 'Senior Sales Representative',
    'Director of Product Management', 'Junior Copywriter',
    'Senior Marketing Coordinator', 'Senior Human Resources Manager',
    'Junior Business Development Associate', 'Senior Account Manager',
    'Senior Researcher', 'Junior HR Coordinator',
    'Director of Finance', 'Junior Marketing Coordinator',
    'Junior Data Scientist', 'Senior Operations Analyst',
    'Senior Human Resources Coordinator', 'Senior UX Designer',
    'Junior Product Manager', 'Senior Marketing Specialist',
    'Senior IT Project Manager', 'Senior Quality Assurance Analyst',
    'Director of Sales and Marketing', 'Senior Account Executive',
    'Director of Business Development', 'Junior Social Media Manager',
    'Senior Human Resources Specialist', 'Senior Data Analyst',
    'Director of Human Capital', 'Junior Advertising Coordinator',
    'Junior UX Designer', 'Senior Marketing Director',
    'Senior IT Consultant', 'Senior Financial Advisor',
    'Junior Business Operations Analyst',
    'Junior Social Media Specialist',
    'Senior Product Development Manager', 'Junior Operations Manager',
    'Senior Software Architect', 'Junior Research Scientist',
    'Senior Financial Manager', 'Senior HR Specialist',
    'Senior Data Engineer', 'Junior Operations Coordinator',
    'Director of HR', 'Senior Operations Coordinator',
    'Junior Financial Advisor', 'Director of Engineering',
    'Software Engineer Manager', 'Back end Developer',
    'Senior Project Engineer', 'Full Stack Engineer',
    'Front end Developer', 'Front End Developer',
    'Director of Data Science', 'Human Resources Coordinator',
    'Junior Sales Associate', 'Human Resources Manager',
    'Junior HR Generalist', 'Junior HR Coordinator',
    'Digital Marketing Specialist', 'Receptionist',
    'Marketing Director', 'Social Media Manager', 'Delivery Driver'
    ]

    with st.form("prediction_form"):
        full_name = st.text_input("Full Name")
        age = st.number_input("Age", min_value=18, max_value=60, step=1)
        education_level = st.selectbox("Education Level", ["High School", "Bachelor's Degree", "Master's Degree", "PhD"])
        job_title = st.selectbox("Job Title", options=job_titles_list)
        experience = st.number_input("Years of Experience", min_value=1, max_value=10, step=1)
        
        submitted = st.form_submit_button("Predict Salary")

        if submitted:
            if not full_name.strip():
                st.warning("⚠️ Please enter your full name before predicting.")
            else:
                salary = predict_salary(age, experience, education_level, job_title)
                st.markdown(
                    f"""
                    <div style='
                    background-color: #ecfdf5;
                    color: #065f46;
                    border: 1px solid #34d399;
                    padding: 1rem;
                    text-align: center;
                    font-size: 1.2rem;
                    font-weight: 600;
                    border-radius: 10px;
                    '>
                    💰 Estimated Annual Salary for {full_name or 'User'}: <strong>${salary:,.2f}</strong>
                    </div>
                    """,
                    unsafe_allow_html=True
                )



