import streamlit as st
from pathlib import Path
import time

# ─── PAGE META ───────────────────────────────────────────────
st.set_page_config(
    page_title="anushqaa",
    page_icon="assets/lightning.png",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ─── COMPLETE CSS STYLING ───────────────────────────────────
def load_css():
    # Get the path to the styles.css file
    css_file = Path(__file__).parent / "styles.css"
    # Read and inject CSS
    with open(css_file) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ─── PROJECT DATA ───────────────────────────────────────────
PROJECT_DATA = [
    {
        "title": "The Perfume Atelier: AI Scent Recommender",
        "img": "https://i.pinimg.com/736x/6b/d7/aa/6bd7aa8c01e5f886452df5baefd7ed4e.jpg",
        "desc": "Full-stack perfume recommendation engine combining chatbot preference extraction with FAISS vector search and UMAP visualization.",
        "tags": ["Featured", "Full Stack", "Vector Databases", "Generative AI", "Docker"],
        "demo": "",
        "code": "",
        "details": "Developed Dockerized microservices (FastAPI backend + Streamlit frontend) where DeepSeek chatbot captures user preferences and FAISS provides scent recommendations. Includes interactive UMAP visualization for exploring 500+ perfume embeddings."
    },
    {
        "title": "AskYourBook: Document Intelligence Assistant",
        "img": "https://i.pinimg.com/736x/28/c2/a8/28c2a8b423bc04325ccfcd5a7b39ee45.jpg",
        "desc": "RAG system using LLaMA 3.3 and ChromaDB for textbook-grade Q&A from PDFs.",
        "tags": ["Featured", "NLP", "Vector Databases", "Generative AI"],
        "demo": "",
        "code": "",
        "details": "Processed documents into semantic chunks using intelligent chunking, generated embeddings via ChromaDB, and fine-tuned LLaMA 3.3 for contextual answers with citation support."
    },
    {
        "title": "GreenHeart: AI Plant Doctor",
        "img": "https://i.pinimg.com/736x/19/56/42/1956421058fc79d87d5a2f83b4afd2b6.jpg",
        "desc": "Dual-service Streamlit app diagnosing plant diseases using Gemini Pro and custom YOLOv8 segmentation.",
        "tags": ["Featured", "Computer Vision", "Generative AI", "Cloud API"],
        "demo": "",
        "code": "",
        "details": "Integrated Google Gemini 2.5 Pro for disease analysis while fine-tuning YOLOv8-nano (tracked with Weights & Biases) for precise infection segmentation. Provides treatment advice and visual annotations in real-time diagnostics."
    },
    {
        "title": "Drone Imagery Segmentor",
        "img": "https://i.pinimg.com/736x/8f/28/17/8f28171b0b405a2cb1a8e74119f9c712.jpg",
        "desc": "Aerial image analysis system benchmarking 7 segmentation models for terrain feature extraction.",
        "tags": ["Featured", "Computer Vision", "Deep Learning"],
        "demo": "",
        "code": "",
        "details": "Evaluated UNet++, FPN, DeepLabV3+ and SegFormer architectures with data augmentation. Selected ResNet50-backed UNet++ for optimal IoU performance on environmental monitoring tasks."
    },
    {
        "title": "Intelligent FAQ Chatbot",
        "img": "https://i.pinimg.com/736x/3b/ea/2e/3bea2ede87745c4e0027f5da20487743.jpg",
        "desc": "RAG system using Pinecone and LangChain for dynamic knowledge base interactions.",
        "tags": ["NLP", "Vector Databases", "Web Scraping"],
        "demo": "",
        "code": "",
        "details": "Scraped web data, processed with LLM chunking, stored in Pinecone vector DB, and implemented low-latency similarity search for accurate FAQ retrieval."
    },
]

# ─── ARTICLE DATA ────────────────────────────────────────────
ARTICLE_DATA = [
    
    {
        "emoji": "🤖v",
        "title": "Building Intelligent Web Apps",
        "date": "December 2024",
        "desc": "How to integrate machine learning models into modern web applications using Streamlit and FastAPI."
    },
    {
        "emoji": "🤖",
        "title": "Building Intelligent Web Apps",
        "date": "December 2024",
        "desc": "How to integrate machine learning models into modern web applications using Streamlit and FastAPI."
    },
    {
        "emoji": "🤖",
        "title": "Building Intelligent Web Apps",
        "date": "December 2024",
        "desc": "How to integrate machine learning models into modern web applications using Streamlit and FastAPI."
    },
]

# ─── PROJECT FUNCTIONS ──────────────────────────────────────
def create_project_card(project, index):
    tags = " ".join(f'<span class="tag">{t}</span>' for t in project["tags"])
    return f"""
    <div class="proj-card" style="animation-delay: {index * 0.1}s">
        <div class="proj-card-inner">
            <div class="proj-card-front">
                <img src="{project['img']}" alt="{project['title']}"/>
                <div class="pc-body">
                    <h3>{project['title']}</h3>
                    <p>{project['desc']}</p>
                    <div class="tag-list">{tags}</div>
                </div>
            </div>
            <div class="proj-card-back">
                <h3>{project['title']}</h3>
                <p>{project['details']}</p>
                <div class="btn-row">
                    <a href="{project['demo']}" target="_blank" class="btn">Demo</a>
                    <a href="{project['code']}" target="_blank" class="btn">Code</a>
                </div>
            </div>
        </div>
    </div>
    """

def show_projects():
    st.html('<div class="section" id="projects"><h2 class="section-title">Projects</h2>')
    
    # Filter tags
    all_tags = set()
    for project in PROJECT_DATA:
        all_tags.update(project["tags"])
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        selected_tag = st.selectbox(
            "Filter by technology:",
            ["All"] + sorted(list(all_tags)),
            key="project_filter"
        )
    
    # Filter projects
    if selected_tag == "All":
        filtered_projects = PROJECT_DATA
    else:
        filtered_projects = [p for p in PROJECT_DATA if selected_tag in p["tags"]]
    
    # Display projects in grid
    cards_html = ""
    for i, project in enumerate(filtered_projects):
        cards_html += create_project_card(project, i)
    
    st.html(f'<div class="proj-grid-container">{cards_html}</div></div>')

# ─── ARTICLE CAROUSEL ───────────────────────────────────────
def show_articles():
    st.html('<div class="section" id="articles"><h2 class="section-title">Latest Articles</h2>')
    
    # Generate article cards HTML
    articles_html = ""
    for article in ARTICLE_DATA:
        articles_html += f"""
        <div class="article-card glass">
            <div class="emoji">{article['emoji']}</div>
            <h3>{article['title']}</h3>
            <div class="date">{article['date']}</div>
            <p>{article['desc']}</p>
            <a href="#" class="btn">Read More</a>
        </div>
        """
    
    # Carousel container
    st.html(f"""
    <div class="articles-section">
        <div class="carousel-container">
            <div class="carousel" id="article-carousel">
                {articles_html}
            </div>
            <div class="carousel-controls">
                <button class="carousel-btn" onclick="slideCarousel(-1)"><i class="fas fa-chevron-left"></i></button>
                <button class="carousel-btn" onclick="slideCarousel(1)"><i class="fas fa-chevron-right"></i></button>
            </div>
        </div>
    </div>
    </div>
    """)
    
    # Carousel JavaScript
    st.components.v1.html("""
    <script>
    let currentSlide = 0;
    const slides = document.querySelectorAll('.article-card');
    const slideCount = slides.length;
    const visibleSlides = window.innerWidth < 768 ? 1 : (window.innerWidth < 1024 ? 2 : 3);
    
    function slideCarousel(direction) {
        currentSlide = (currentSlide + direction + slideCount) % slideCount;
        
        // Only move if there are more slides than visible
        if (slideCount > visibleSlides) {
            const carousel = document.getElementById('article-carousel');
            const slideWidth = slides[0].offsetWidth + 32; // width + gap
            const transformValue = -currentSlide * slideWidth;
            carousel.style.transform = `translateX(${transformValue}px)`;
        }
    }
    
    // Initialize carousel position
    slideCarousel(0);
    </script>
    """, height=0)

# ─── SECTION FUNCTIONS ──────────────────────────────────────
def hero():
    st.html("""
    <div class="hero fade-up">
        <div class="hero-nav" id="navbar">
            <div class="nav-logo"><i class="fas fa-cube"></i> Portfolio</div>
            <div class="nav-links">
                <a href="#about" class="nav-link">About</a>
                <a href="#projects" class="nav-link">Projects</a>
                <a href="#articles" class="nav-link">Articles</a>
                <a href="#contact" class="nav-link">Contact</a>
            </div>
            <a href="#contact" class="contact-btn">Get in touch</a>
        </div>
        
        <div class="floating-icons">
            <div class="floating-icon icon-1"><i class="fas fa-cube"></i></div>
            <div class="floating-icon icon-2"><i class="fas fa-atom"></i></div>
            <div class="floating-icon icon-3"><i class="fas fa-shapes"></i></div>
            <div class="floating-icon icon-4"><i class="fas fa-circle"></i></div>
        </div>
        
        <div class="hero-content">
            <div class="hero-intro">Hello, I'm</div>
            <h1 class="hero-statement">
                <span class="hero-highlight">Anushka Shekhawat</span><br>
                Building Full-Stack <br>
                AI Solutions<br>
            </h1>
            <div class="hero-cta">
                <a href="#projects" class="cta-link"><i class="fas fa-code"></i> View my work</a>
                <span class="cta-separator">—</span>
                <a href="#contact" class="cta-link"><i class="fas fa-paper-plane"></i> Contact me</a>
            </div>
        </div>
        
        <div class="social-sidebar">
            <a href="#" class="social-minimal">GitHub</a>
            <a href="#" class="social-minimal">LinkedIn</a>
            <a href="#" class="social-minimal">Twitter</a>
        </div>
        
        <div class="geo-accent"></div>
        
        <div class="scroll-hint">
            <div class="scroll-line"></div>
        </div>
    </div>
    """)

def about():
    st.html("""
    <div class="about-section fade-up" id="about">
        <div class="about-icons">
            <div class="about-icon ai-icon-1"><i class="fas fa-brain"></i></div>
            <div class="about-icon ai-icon-2"><i class="fas fa-robot"></i></div>
            <div class="about-icon ai-icon-3"><i class="fas fa-microchip"></i></div>
        </div>
        
        <div class="about-container">
            <div class="section-number">01</div>
            
            <div class="about-content">
                <h2 class="about-title">About Me</h2>
                
                <p class="about-intro">
                    I build smart systems that understand data and make decisions. 
                </p>
                
                <p class="about-detail">
                    As an ML engineer who also speaks data science and software fluently, 
                    I connect the dots between algorithms, insights, and production-ready code.
                </p>
                
                <p class="about-detail">
                    By blending <span class="highlight">Machine Learning, analytics, and software skills</span>, 
                    I build full-stack solutions that actually work in the real world.
                    From vector-powered recommendation engines to real-time Computer Vision inference APIs, 
                    I build solutions that make AI accessible and delightful to use.
                </p>
                
                <div class="skills-grid">
                    <div class="skill-category">
                        <div class="skill-label">AI & Machine Learning</div>
                        <div class="skill-items">PyTorch • Transformers • LLMs • Computer Vision • Generative AI</div>
                    </div>
                    <div class="skill-category">
                        <div class="skill-label">Data & Analytics</div>
                        <div class="skill-items">SQL • Pandas • Statistical Modeling • EDA • Predictive Analytics</div>
                    </div>
                    <div class="skill-category">
                        <div class="skill-label">Software Engineering</div>
                        <div class="skill-items">Python • REST APIs • Docker • Microservices • System Design</div>
                    </div>
                    <div class="skill-category">
                        <div class="skill-label">Deployment & Ops</div>
                        <div class="skill-items">AWS • CI/CD • MLOps • LangChain • RAG Architectures</div>
                    </div>
                </div>
            </div>
                
                <!-- Code snippet moved below skills grid -->
                <div class="code-snippet-container">
                    <div class="code-snippet">
                        <div class="code-line"><span class="code-comment"># Building intelligent solutions</span></div>
                        <div class="code-line"><span class="code-keyword">class</span> <span class="code-function">ML_Engineer</span>:</div>
                        <div class="code-line">    <span class="code-keyword">def</span> <span class="code-function">__init__</span>(<span class="code-name">self</span>):</div>
                        <div class="code-line">        <span class="code-name">self.skills</span> = [</div>
                        <div class="code-line">            <span class="code-string">"transformers"</span>,</div>
                        <div class="code-line">            <span class="code-string">"computer_vision"</span>,</div>
                        <div class="code-line">            <span class="code-string">"cloud_deployment"</span></div>
                        <div class="code-line">        ]</div>
                        <div class="code-line">    </div>
                        <div class="code-line">    <span class="code-keyword">def</span> <span class="code-function">build</span>(<span class="code-name">self</span>):</div>
                        <div class="code-line">        <span class="code-keyword">return</span> <span class="code-string">"AI systems that solve real problems"</span></div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    """)

def contact():
    st.html("""
    <div class="section fade-up" id="contact">
        <h2 class="section-title">Get In Touch</h2>
        <div class="contact-form">
            <p style="text-align: center; margin-bottom: 2rem; color: #666;">
                Let's collaborate on something amazing together.
            </p>
        </div>
    </div>
    """)
    
    # Streamlit contact form
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        with st.form("contact_form"):
            name = st.text_input("Your Name")
            email = st.text_input("Your Email")
            message = st.text_area("Your Message", height=150)
            submitted = st.form_submit_button("Send Message", use_container_width=True)
            
            if submitted:
                if name and email and message:
                    st.success("✅ Thank you! Your message has been sent successfully.")
                    st.balloons()
                else:
                    st.error("❌ Please fill in all fields.")

# ─── SCROLL REVEAL FUNCTIONALITY ────────────────────────────
def add_scroll_reveal():
    st.components.v1.html("""
    <script>
    // Scroll spy for navigation
    window.addEventListener('scroll', function() {
        const navbar = document.getElementById('navbar');
        if (window.scrollY > 50) {
            navbar.classList.add('nav-scrolled');
        } else {
            navbar.classList.remove('nav-scrolled');
        }
    });
    
    // Scroll reveal animation
    function addScrollReveal() {
        const observerOptions = {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        };
        
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('is-visible');
                }
            });
        }, observerOptions);
        
        document.querySelectorAll('.fade-up').forEach(el => {
            observer.observe(el);
        });
    }
    
    // Run when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', addScrollReveal);
    } else {
        addScrollReveal();
    }
    </script>
    """, height=0)

# ─── MAIN APPLICATION ───────────────────────────────────────
def main():
    # Load CSS
    load_css()
    
    # Render sections in order
    hero()
    about()
    show_projects()
    # show_articles()
    contact()
    
    # Add scroll reveal functionality
    add_scroll_reveal()
    
    # Footer
    st.html("""
    <footer class="footer">
        <div class="section">
            © 2025 anushqa.
        </div>
    </footer>
    """)

if __name__ == "__main__":
    main()