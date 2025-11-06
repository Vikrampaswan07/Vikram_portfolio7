# # app.py — Pixel-identical Streamlit version of your HTML portfolio
# import base64
# from pathlib import Path
# from PIL import Image
# import io
# import streamlit as st
# import streamlit.components.v1 as components

# st.set_page_config(page_title="Vikram Kumar | Data Science Portfolio",
#                    page_icon="🐍", layout="wide", initial_sidebar_state="collapsed")

# # ---- load your photo and convert to a data URL so it renders inside the component
# IMAGE_PATH = Path("vikramPhoto.jpg")  # change if needed

# def image_to_data_url(p: Path) -> str:
#     if not p.exists():
#         # simple fallback placeholder if the path is wrong
#         return "https://placehold.co/200x200/4B5563/FFFFFF?text=Vikram"
#     img = Image.open(p).convert("RGB")
#     buf = io.BytesIO()
#     img.save(buf, format="JPEG", quality=92)
#     b64 = base64.b64encode(buf.getvalue()).decode("utf-8")
#     return f"data:image/jpeg;base64,{b64}"

# img_src = image_to_data_url(IMAGE_PATH)

# # ---- the HTML from your working site, unchanged in appearance ----
# html = f"""
# <!DOCTYPE html>
# <html lang="en">
# <head>
# <meta charset="UTF-8" />
# <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
# <title>Vikram Kumar | Data Science Portfolio</title>

# <!-- Tailwind CSS -->
# <script src="https://cdn.tailwindcss.com"></script>
# <!-- Three.js -->
# <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>

# <style>
#   body {{
#     font-family: 'Inter', sans-serif;
#     margin: 0;
#     overflow: hidden; /* Hide scrollbars due to 3D canvas */
#     background: #111827; /* ensure same dark base as your screenshot */
#   }}
#   #three-canvas {{
#     position: fixed;
#     top: 0; left: 0;
#     width: 100vw; height: 100vh;
#     z-index: 0;
#   }}
#   #content-overlay {{
#     position: relative;
#     z-index: 10;
#     width: 90%;
#     max-width: 1200px;
#     height: 90vh;
#     margin: 5vh auto;
#     border-radius: 1.5rem;
#     backdrop-filter: blur(10px);
#     box-shadow: 0 10px 30px rgba(0,0,0,0.5);
#     padding: 2rem;
#     background-color: rgba(17, 24, 39, 0.85);
#   }}
#   .portfolio-grid {{
#     display: flex;
#     flex-direction: column;
#     gap: 2rem;
#     height: 100%;
#   }}
#   @media (min-width: 768px) {{
#     .portfolio-grid {{ flex-direction: row; }}
#   }}
#   .text-readable {{ color: #E5E7EB; }}
# </style>
# </head>

# <body class="bg-gray-900">
#   <!-- Revolving background -->
#   <canvas id="three-canvas"></canvas>

#   <!-- Content card -->
#   <div id="content-overlay" class="text-readable">
#     <div class="portfolio-grid">

#       <!-- LEFT: Photo -->
#       <div class="md:w-1/4 w-full flex justify-center md:justify-start">
#         <div class="p-4 bg-gray-800 rounded-xl shadow-lg">
#           <img src="{img_src}"
#                alt="Vikram Kumar's Professional Photo"
#                class="w-48 h-48 md:w-full md:h-auto rounded-xl object-cover border-4 border-yellow-500 shadow-xl" />
#           <p class="mt-2 text-center text-sm font-light text-gray-400">Data Analyst & Scientist</p>
#         </div>
#       </div>

#       <!-- RIGHT: Name + Summary -->
#       <div class="md:w-3/4 w-full overflow-y-auto pr-2">
#         <div class="border-b border-gray-700 pb-4 mb-6">
#           <h1 class="text-5xl font-extrabold text-blue-400 tracking-tight">Vikram Kumar</h1>
#           <p class="text-xl font-medium text-yellow-500 mt-1">
#             Fresher | Data Analyst | Data Scientist | Machine Learning Engineer
#           </p>
#         </div>

#         <section class="mb-8">
#           <h2 class="text-2xl font-semibold border-l-4 border-blue-400 pl-3 mb-4 text-gray-100">
#             Professional Summary
#           </h2>
#           <p class="text-lg leading-relaxed">
#             Highly motivated and results-driven aspiring Data Scientist and Analyst proficient in leveraging Python
#             (Pandas, NumPy) and SQL to transform raw data into actionable business insights. Possessing a strong
#             foundation in algorithms, data structures, and statistical analysis, I combine academic rigor with
#             practical experience in building and deploying machine learning models (e.g., achieving 85% accuracy
#             in a Movie Recommendation System). Experienced in creating end-to-end data products, including
#             developing ETL pipelines for real-time data integration and deploying interactive visualizations via
#             Power BI, Streamlit, and Matplotlib. Highly interested in Generative AI and RAG Pipelines, and actively
#             seeking to apply analytical expertise to drive data-driven decision-making.
#           </p>
#         </section>

#         <section class="mb-8">
#           <h2 class="text-2xl font-semibold border-l-4 border-yellow-500 pl-3 mb-4 text-gray-100">Core Skills</h2>
#           <div class="flex flex-wrap gap-2">
#             <span class="bg-blue-600 text-white text-sm font-medium px-3 py-1 rounded-full shadow-md">Python</span>
#             <span class="bg-blue-600 text-white text-sm font-medium px-3 py-1 rounded-full shadow-md">Data Structure & Algorithms</span>
#             <span class="bg-blue-600 text-white text-sm font-medium px-3 py-1 rounded-full shadow-md">Object Oriented Programming</span>
#             <span class="bg-blue-600 text-white text-sm font-medium px-3 py-1 rounded-full shadow-md">Machine Learning</span>
#             <span class="bg-blue-600 text-white text-sm font-medium px-3 py-1 rounded-full shadow-md">SQL/NoSQL</span>
#             <span class="bg-blue-600 text-white text-sm font-medium px-3 py-1 rounded-full shadow-md">Git</span>
#             <span class="bg-yellow-600 text-white text-sm font-medium px-3 py-1 rounded-full shadow-md">GitHub</span>
#             <span class="bg-yellow-600 text-white text-sm font-medium px-3 py-1 rounded-full shadow-md">Cloud (AWS)</span>
#             <span class="bg-yellow-600 text-white text-sm font-medium px-3 py-1 rounded-full shadow-md">ChatGPT</span>
#             <span class="bg-yellow-600 text-white text-sm font-medium px-3 py-1 rounded-full shadow-md">Power BI</span>
#             <span class="bg-yellow-600 text-white text-sm font-medium px-3 py-1 rounded-full shadow-md">Data Visualization</span>
#             <span class="bg-yellow-600 text-white text-sm font-medium px-3 py-1 rounded-full shadow-md">MS power point</span>
#           </div>
#         </section>

#       </div>
#     </div>
#   </div>

#   <!-- Three.js background: two intertwined “snakes” -->
#   <script>
#     let scene, camera, renderer, snakeBlue, snakeGreen;
#     const canvas = document.getElementById('three-canvas');

#     function init() {{
#       scene = new THREE.Scene();
#       camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
#       camera.position.z = 5;

#       renderer = new THREE.WebGLRenderer({{ canvas: canvas, antialias: true, alpha: true }});
#       renderer.setSize(window.innerWidth, window.innerHeight);
#       renderer.setClearColor(0x111827, 1);

#       const ambientLight = new THREE.AmbientLight(0x404040);
#       scene.add(ambientLight);
#       const directionalLight = new THREE.DirectionalLight(0xffffff, 0.8);
#       directionalLight.position.set(0, 10, 5).normalize();
#       scene.add(directionalLight);

#       const geometry = new THREE.TorusKnotGeometry(1.5, 0.25, 200, 30);

#       const materialBlue = new THREE.MeshPhongMaterial({{
#         color: 0x4B8BBE, specular: 0xffffff, shininess: 120, emissive: 0x000000, transparent: true, opacity: 0.9
#       }});
#       snakeBlue = new THREE.Mesh(geometry, materialBlue);
#       snakeBlue.position.set(0.1, 0.1, 0);
#       scene.add(snakeBlue);

#       const materialGreen = new THREE.MeshPhongMaterial({{
#         color: 0x64CC34, specular: 0xffffff, shininess: 120, emissive: 0x000000, transparent: true, opacity: 0.9
#       }});
#       snakeGreen = new THREE.Mesh(geometry, materialGreen);
#       snakeGreen.position.set(-0.1, -0.1, 0);
#       snakeGreen.rotation.set(Math.PI / 4, 0, 0);
#       scene.add(snakeGreen);
#     }}

#     function animate() {{
#       requestAnimationFrame(animate);
#       snakeBlue.rotation.x += 0.004;
#       snakeBlue.rotation.y += 0.007;

#       snakeGreen.rotation.x -= 0.002;
#       snakeGreen.rotation.y -= 0.005;
#       snakeGreen.rotation.z += 0.003;

#       const rockX = Math.sin(Date.now() * 0.0001) * 0.4;
#       const rockY = Math.cos(Date.now() * 0.0001) * 0.4;
#       snakeBlue.position.x = 0.1 + rockX;
#       snakeBlue.position.y = 0.1 + rockY;
#       snakeGreen.position.x = -0.1 - rockX;
#       snakeGreen.position.y = -0.1 - rockY;

#       renderer.render(scene, camera);
#     }}

#     function onWindowResize() {{
#       camera.aspect = window.innerWidth / window.innerHeight;
#       camera.updateProjectionMatrix();
#       renderer.setSize(window.innerWidth, window.innerHeight);
#     }}

#     window.onload = function () {{
#       init();
#       animate();
#       window.addEventListener('resize', onWindowResize, false);
#     }};
#   </script>
# </body>
# </html>
# """

# # render the HTML “as-is” inside Streamlit (no scroll; tall iframe)
# components.html(html, height=900, scrolling=False)





























# # app.py — Streamlit portfolio with footer contacts
# import base64
# from pathlib import Path
# from PIL import Image
# import io
# import streamlit as st
# import streamlit.components.v1 as components

# st.set_page_config(page_title="Vikram Kumar | Data Science Portfolio",
#                    page_icon="🐍", layout="wide", initial_sidebar_state="collapsed")

# # ---- load your photo and convert to a data URL so it renders inside the component
# IMAGE_PATH = Path("vikramPhoto.jpg")  # change if needed

# def image_to_data_url(p: Path) -> str:
#     if not p.exists():
#         # simple fallback placeholder if the path is wrong
#         return "https://placehold.co/200x200/4B5563/FFFFFF?text=Vikram"
#     img = Image.open(p).convert("RGB")
#     buf = io.BytesIO()
#     img.save(buf, format="JPEG", quality=92)
#     b64 = base64.b64encode(buf.getvalue()).decode("utf-8")
#     return f"data:image/jpeg;base64,{b64}"

# img_src = image_to_data_url(IMAGE_PATH)

# # ---- HTML (appearance kept; footer added) ----
# html = f"""
# <!DOCTYPE html>
# <html lang="en">
# <head>
# <meta charset="UTF-8" />
# <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
# <title>Vikram Kumar | Data Science Portfolio</title>

# <!-- Tailwind CSS -->
# <script src="https://cdn.tailwindcss.com"></script>
# <!-- Three.js -->
# <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>

# <style>
#   body {{
#     font-family: 'Inter', sans-serif;
#     margin: 0;
#     overflow: hidden; /* Hide scrollbars due to 3D canvas */
#     background: #111827; /* keep same dark base */
#   }}
#   #three-canvas {{
#     position: fixed;
#     top: 0; left: 0;
#     width: 100vw; height: 100vh;
#     z-index: 0;
#   }}
#   #content-overlay {{
#     position: relative;
#     z-index: 10;
#     width: 90%;
#     max-width: 1200px;
#     height: 90vh;
#     margin: 5vh auto;
#     border-radius: 1.5rem;
#     backdrop-filter: blur(10px);
#     box-shadow: 0 10px 30px rgba(0,0,0,0.5);
#     padding: 2rem;
#     background-color: rgba(17, 24, 39, 0.85);
#     overflow-y: auto; /* allow scrolling to see footer if needed */
#   }}
#   .portfolio-grid {{
#     display: flex;
#     flex-direction: column;
#     gap: 2rem;
#     height: auto;
#   }}
#   @media (min-width: 768px) {{
#     .portfolio-grid {{ flex-direction: row; }}
#   }}
#   .text-readable {{ color: #E5E7EB; }}
#   .footer-link:hover {{ opacity: .9; }}
# </style>
# </head>

# <body class="bg-gray-900">
#   <!-- Revolving background -->
#   <canvas id="three-canvas"></canvas>

#   <!-- Content card -->
#   <div id="content-overlay" class="text-readable">
#     <div class="portfolio-grid">

#       <!-- LEFT: Photo -->
#       <div class="md:w-1/4 w-full flex justify-center md:justify-start">
#         <div class="p-4 bg-gray-800 rounded-xl shadow-lg">
#           <img src="{img_src}"
#                alt="Vikram Kumar's Professional Photo"
#                class="w-48 h-48 md:w-full md:h-auto rounded-xl object-cover border-4 border-yellow-500 shadow-xl" />
#           <p class="mt-2 text-center text-sm font-light text-gray-400">Data Analyst & Scientist</p>
#         </div>
#       </div>

#       <!-- RIGHT: Name + Summary -->
#       <div class="md:w-3/4 w-full overflow-y-auto pr-2">
#         <div class="border-b border-gray-700 pb-4 mb-6">
#           <h1 class="text-5xl font-extrabold text-blue-400 tracking-tight">Vikram Kumar</h1>
#           <p class="text-xl font-medium text-yellow-500 mt-1">
#             Fresher | Data Analyst | Data Scientist | Machine Learning Engineer
#           </p>
#         </div>

#         <section class="mb-8">
#           <h2 class="text-2xl font-semibold border-l-4 border-blue-400 pl-3 mb-4 text-gray-100">
#             Professional Summary
#           </h2>
#           <p class="text-lg leading-relaxed">
#             Highly motivated and results-driven aspiring Data Scientist and Analyst proficient in leveraging Python
#             (Pandas, NumPy) and SQL to transform raw data into actionable business insights. Possessing a strong
#             foundation in algorithms, data structures, and statistical analysis, I combine academic rigor with
#             practical experience in building and deploying machine learning models (e.g., achieving 85% accuracy
#             in a Movie Recommendation System). Experienced in creating end-to-end data products, including
#             developing ETL pipelines for real-time data integration and deploying interactive visualizations via
#             Power BI, Streamlit, and Matplotlib. Highly interested in Generative AI and RAG Pipelines, and actively
#             seeking to apply analytical expertise to drive data-driven decision-making.
#           </p>
#         </section>

#         <section class="mb-8">
#           <h2 class="text-2xl font-semibold border-l-4 border-yellow-500 pl-3 mb-4 text-gray-100">Core Skills</h2>
#           <div class="flex flex-wrap gap-2">
#             <span class="bg-blue-600 text-white text-sm font-medium px-3 py-1 rounded-full shadow-md">Python</span>
#             <span class="bg-blue-600 text-white text-sm font-medium px-3 py-1 rounded-full shadow-md">Data Structure & Algorithms</span>
#             <span class="bg-blue-600 text-white text-sm font-medium px-3 py-1 rounded-full shadow-md">Object Oriented Programming</span>
#             <span class="bg-blue-600 text-white text-sm font-medium px-3 py-1 rounded-full shadow-md">Machine Learning</span>
#             <span class="bg-blue-600 text-white text-sm font-medium px-3 py-1 rounded-full shadow-md">SQL/NoSQL</span>
#             <span class="bg-blue-600 text-white text-sm font-medium px-3 py-1 rounded-full shadow-md">Git</span>
#             <span class="bg-yellow-600 text-white text-sm font-medium px-3 py-1 rounded-full shadow-md">GitHub</span>
#             <span class="bg-yellow-600 text-white text-sm font-medium px-3 py-1 rounded-full shadow-md">Cloud (AWS)</span>
#             <span class="bg-yellow-600 text-white text-sm font-medium px-3 py-1 rounded-full shadow-md">ChatGPT</span>
#             <span class="bg-yellow-600 text-white text-sm font-medium px-3 py-1 rounded-full shadow-md">Power BI</span>
#             <span class="bg-yellow-600 text-white text-sm font-medium px-3 py-1 rounded-full shadow-md">Data Visualization</span>
#             <span class="bg-yellow-600 text-white text-sm font-medium px-3 py-1 rounded-full shadow-md">MS power point</span>
#           </div>
#         </section>

#       </div>
#     </div>

#     <!-- ===== Footer (Contacts) ===== -->
#     <footer class="mt-8 pt-4 border-t border-gray-700">
#       <div class="flex flex-wrap items-center gap-4 text-sm">
#         <!-- Email -->
#         <a class="footer-link inline-flex items-center gap-2 text-gray-200"
#            href="mailto:your.email@example.com" target="_blank" rel="noopener">
#           <span class="inline-block w-5 h-5 rounded bg-blue-600 grid place-items-center text-white">✉</span>
#           your.email@example.com
#         </a>
#         <!-- LinkedIn -->
#         <a class="footer-link inline-flex items-center gap-2 text-blue-400"
#            href="https://www.linkedin.com/in/your-handle" target="_blank" rel="noopener">
#           <span class="inline-block w-5 h-5 rounded bg-blue-600 grid place-items-center text-white">in</span>
#           linkedin.com/in/your-handle
#         </a>
#         <!-- Instagram -->
#         <a class="footer-link inline-flex items-center gap-2 text-pink-300"
#            href="https://www.instagram.com/your_username" target="_blank" rel="noopener">
#           <span class="inline-block w-5 h-5 rounded bg-pink-600 grid place-items-center text-white">◎</span>
#           @your_username
#         </a>
#         <!-- Facebook -->
#         <a class="footer-link inline-flex items-center gap-2 text-blue-300"
#            href="https://www.facebook.com/your.profile" target="_blank" rel="noopener">
#           <span class="inline-block w-5 h-5 rounded bg-blue-700 grid place-items-center text-white">f</span>
#           facebook.com/your.profile
#         </a>
#       </div>
#     </footer>
#     <!-- ===== End Footer ===== -->

#   </div>

#   <!-- Three.js background: two intertwined “snakes” -->
#   <script>
#     let scene, camera, renderer, snakeBlue, snakeGreen;
#     const canvas = document.getElementById('three-canvas');

#     function init() {{
#       scene = new THREE.Scene();
#       camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
#       camera.position.z = 5;

#       renderer = new THREE.WebGLRenderer({{ canvas: canvas, antialias: true, alpha: true }});
#       renderer.setSize(window.innerWidth, window.innerHeight);
#       renderer.setClearColor(0x111827, 1);

#       const ambientLight = new THREE.AmbientLight(0x404040);
#       scene.add(ambientLight);
#       const directionalLight = new THREE.DirectionalLight(0xffffff, 0.8);
#       directionalLight.position.set(0, 10, 5).normalize();
#       scene.add(directionalLight);

#       const geometry = new THREE.TorusKnotGeometry(1.5, 0.25, 200, 30);

#       const materialBlue = new THREE.MeshPhongMaterial({{
#         color: 0x4B8BBE, specular: 0xffffff, shininess: 120, emissive: 0x000000, transparent: true, opacity: 0.9
#       }});
#       snakeBlue = new THREE.Mesh(geometry, materialBlue);
#       snakeBlue.position.set(0.1, 0.1, 0);
#       scene.add(snakeBlue);

#       const materialGreen = new THREE.MeshPhongMaterial({{
#         color: 0x64CC34, specular: 0xffffff, shininess: 120, emissive: 0x000000, transparent: true, opacity: 0.9
#       }});
#       snakeGreen = new THREE.Mesh(geometry, materialGreen);
#       snakeGreen.position.set(-0.1, -0.1, 0);
#       snakeGreen.rotation.set(Math.PI / 4, 0, 0);
#       scene.add(snakeGreen);
#     }}

#     function animate() {{
#       requestAnimationFrame(animate);
#       snakeBlue.rotation.x += 0.004;
#       snakeBlue.rotation.y += 0.007;

#       snakeGreen.rotation.x -= 0.002;
#       snakeGreen.rotation.y -= 0.005;
#       snakeGreen.rotation.z += 0.003;

#       const rockX = Math.sin(Date.now() * 0.0001) * 0.4;
#       const rockY = Math.cos(Date.now() * 0.0001) * 0.4;
#       snakeBlue.position.x = 0.1 + rockX;
#       snakeBlue.position.y = 0.1 + rockY;
#       snakeGreen.position.x = -0.1 - rockX;
#       snakeGreen.position.y = -0.1 - rockY;

#       renderer.render(scene, camera);
#     }}

#     function onWindowResize() {{
#       camera.aspect = window.innerWidth / window.innerHeight;
#       camera.updateProjectionMatrix();
#       renderer.setSize(window.innerWidth, window.innerHeight);
#     }}

#     window.onload = function () {{
#       init();
#       animate();
#       window.addEventListener('resize', onWindowResize, false);
#     }};
#   </script>
# </body>
# </html>
# """

# # render the HTML “as-is” inside Streamlit (no scroll; tall iframe)
# components.html(html, height=900, scrolling=False)



















# app.py — Streamlit portfolio (no outer black border, full-screen design)
import base64
from pathlib import Path
from PIL import Image
import io
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Vikram Kumar | Data Science Portfolio",
                   page_icon="🐍", layout="wide", initial_sidebar_state="collapsed")

# ---- load your photo and convert to a data URL ----
IMAGE_PATH = Path("vikramPhoto.jpg")  # change if needed

def image_to_data_url(p: Path) -> str:
    if not p.exists():
        return "https://placehold.co/200x200/4B5563/FFFFFF?text=Vikram"
    img = Image.open(p).convert("RGB")
    buf = io.BytesIO()
    img.save(buf, format="JPEG", quality=92)
    b64 = base64.b64encode(buf.getvalue()).decode("utf-8")
    return f"data:image/jpeg;base64,{b64}"

img_src = image_to_data_url(IMAGE_PATH)

# ---- Updated HTML (removed outer black border) ----
html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>Vikram Kumar | Data Science Portfolio</title>

<!-- Tailwind CSS -->
<script src="https://cdn.tailwindcss.com"></script>
<!-- Three.js -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>

<style>
  html, body {{
    margin: 0;
    padding: 0;
    height: 100%;
    width: 100%;
    overflow: hidden;
    font-family: 'Inter', sans-serif;
    background: transparent !important; /* 🔹 Removes the black background */
  }}
  #three-canvas {{
    position: fixed;
    top: 0; left: 0;
    width: 100vw; height: 100vh;
    z-index: 0;
  }}
  #content-overlay {{
    position: absolute;
    top: 0; left: 0;
    width: 100%;
    height: 100%;
    border-radius: 0; /* no border radius */
    backdrop-filter: blur(10px);
    box-shadow: none; /* remove shadow border */
    padding: 2rem 4rem;
    background-color: rgba(17, 24, 39, 0.85); /* slightly transparent */
    display: flex;
    justify-content: center;
    align-items: center;
  }}
  .portfolio-grid {{
    display: flex;
    flex-direction: column;
    gap: 2rem;
    width: 100%;
    max-width: 1200px;
  }}
  @media (min-width: 768px) {{
    .portfolio-grid {{ flex-direction: row; }}
  }}
  .text-readable {{ color: #E5E7EB; }}
  .footer-link:hover {{ opacity: .9; }}
</style>
</head>

<body>
  <!-- Rotating Python Snake Background -->
  <canvas id="three-canvas"></canvas>

  <!-- Main Content -->
  <div id="content-overlay" class="text-readable">
    <div class="portfolio-grid">

      <!-- LEFT: Photo -->
      <div class="md:w-1/4 w-full flex justify-center md:justify-start">
        <div class="p-4 bg-gray-800 rounded-xl shadow-lg">
          <img src="{img_src}" alt="Vikram Kumar"
               class="w-48 h-48 md:w-full md:h-auto rounded-xl object-cover border-4 border-yellow-500 shadow-xl" />
          <p class="mt-2 text-center text-sm font-light text-gray-400">Data Analyst & Scientist</p>
        </div>
      </div>

      <!-- RIGHT: Info -->
      <div class="md:w-3/4 w-full overflow-y-auto pr-2">
        <div class="border-b border-gray-700 pb-4 mb-6">
          <h1 class="text-5xl font-extrabold text-blue-400 tracking-tight">Vikram Kumar</h1>
          <p class="text-xl font-medium text-yellow-500 mt-1">
            Fresher | Data Analyst | Data Scientist | Machine Learning Engineer
          </p>
        </div>

        <!-- Summary -->
        <section class="mb-8">
          <h2 class="text-2xl font-semibold border-l-4 border-blue-400 pl-3 mb-4 text-gray-100">Professional Summary</h2>
          <p class="text-lg leading-relaxed">
            Highly motivated and results-driven aspiring Data Scientist and Analyst proficient in leveraging Python
            (Pandas, NumPy) and SQL to transform raw data into actionable business insights. Possessing a strong
            foundation in algorithms, data structures, and statistical analysis, I combine academic rigor with
            practical experience in building and deploying machine learning models (e.g., achieving 85% accuracy
            in a Movie Recommendation System). Experienced in creating end-to-end data products, including
            developing ETL pipelines for real-time data integration and deploying interactive visualizations via
            Power BI, Streamlit, and Matplotlib. Highly interested in Generative AI and RAG Pipelines, and actively
            seeking to apply analytical expertise to drive data-driven decision-making.
          </p>
        </section>

        <!-- Skills -->
        <section class="mb-8">
          <h2 class="text-2xl font-semibold border-l-4 border-yellow-500 pl-3 mb-4 text-gray-100">Core Skills</h2>
          <div class="flex flex-wrap gap-2">
            <span class="bg-blue-600 text-white text-sm font-medium px-3 py-1 rounded-full shadow-md">Python</span>
            <span class="bg-blue-600 text-white text-sm font-medium px-3 py-1 rounded-full shadow-md">Data Structure & Algorithms</span>
            <span class="bg-blue-600 text-white text-sm font-medium px-3 py-1 rounded-full shadow-md">Object Oriented Programming</span>
            <span class="bg-blue-600 text-white text-sm font-medium px-3 py-1 rounded-full shadow-md">Machine Learning</span>
            <span class="bg-blue-600 text-white text-sm font-medium px-3 py-1 rounded-full shadow-md">SQL/NoSQL</span>
            <span class="bg-blue-600 text-white text-sm font-medium px-3 py-1 rounded-full shadow-md">Git</span>
            <span class="bg-yellow-600 text-white text-sm font-medium px-3 py-1 rounded-full shadow-md">GitHub</span>
            <span class="bg-yellow-600 text-white text-sm font-medium px-3 py-1 rounded-full shadow-md">Cloud (AWS)</span>
            <span class="bg-yellow-600 text-white text-sm font-medium px-3 py-1 rounded-full shadow-md">ChatGPT</span>
            <span class="bg-yellow-600 text-white text-sm font-medium px-3 py-1 rounded-full shadow-md">Power BI</span>
            <span class="bg-yellow-600 text-white text-sm font-medium px-3 py-1 rounded-full shadow-md">Data Visualization</span>
            <span class="bg-yellow-600 text-white text-sm font-medium px-3 py-1 rounded-full shadow-md">MS PowerPoint</span>
          </div>
        </section>

        <!-- Footer -->
        <footer class="mt-8 pt-4 border-t border-gray-700 flex flex-wrap gap-4 text-sm">
          <a class="footer-link flex items-center gap-2 text-gray-200" href="mailto:your.email@example.com" target="_blank">
            <span class="inline-block w-5 h-5 rounded bg-blue-600 grid place-items-center text-white">✉</span>
            vikram2021nitjsr@gmail.com
          </a>
          <a class="footer-link flex items-center gap-2 text-blue-400" href="https://www.linkedin.com/in/vikram-kumar-343b98251/" target="_blank">
            <span class="inline-block w-5 h-5 rounded bg-blue-600 grid place-items-center text-white">in</span>
            vikram-kumar-343b98251/
          </a>
                    <!-- GitHub -->
          <a class="footer-link flex items-center gap-2 text-gray-300"
            href="https://github.com/Vikrampaswan07" target="_blank">
            <span class="inline-block w-5 h-5 rounded bg-gray-800 grid place-items-center text-white">
              <svg xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 16 16" class="w-3 h-3">
                <path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 
                7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37
                -2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68
                -.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 
                2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64
                -3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.01.08-2.12 
                0 0 .67-.21 2.2.82A7.54 7.54 0 0 1 8 3.47c.68.003 
                1.36.092 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.11.16 
                1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 
                3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 
                1.93-.01 2.19 0 .21.15.46.55.38A8.012 8.012 
                0 0 0 16 8c0-4.42-3.58-8-8-8z"/>
              </svg>
            </span>
            github.com/Vikrampaswan07
          </a>

          <!-- YouTube -->
          <a class="footer-link flex items-center gap-2 text-red-400"
            href="https://www.youtube.com/@DataWithVikram" target="_blank">
            <span class="inline-block w-5 h-5 rounded bg-red-600 grid place-items-center text-white">
              ▶
            </span>
            youtube.com/@DataWithVikram
          </a>

        </footer>

      </div>
    </div>
  </div>

  <!-- Background animation -->
  <script>
    let scene, camera, renderer, snakeBlue, snakeGreen;
    const canvas = document.getElementById('three-canvas');
    function init() {{
      scene = new THREE.Scene();
      camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
      camera.position.z = 5;
      renderer = new THREE.WebGLRenderer({{ canvas, antialias: true, alpha: true }});
      renderer.setSize(window.innerWidth, window.innerHeight);
      renderer.setClearColor(0x111827, 1);
      const ambient = new THREE.AmbientLight(0x404040);
      scene.add(ambient);
      const dir = new THREE.DirectionalLight(0xffffff, 0.8);
      dir.position.set(0,10,5).normalize();
      scene.add(dir);
      const geo = new THREE.TorusKnotGeometry(1.5,0.25,200,30);
      const matBlue = new THREE.MeshPhongMaterial({{ color:0x4B8BBE, shininess:120, transparent:true, opacity:0.9 }});
      const matGreen = new THREE.MeshPhongMaterial({{ color:0x64CC34, shininess:120, transparent:true, opacity:0.9 }});
      snakeBlue = new THREE.Mesh(geo, matBlue);
      snakeGreen = new THREE.Mesh(geo, matGreen);
      snakeGreen.rotation.set(Math.PI/4,0,0);
      scene.add(snakeBlue);
      scene.add(snakeGreen);
    }}
    function animate() {{
      requestAnimationFrame(animate);
      snakeBlue.rotation.x += 0.004;
      snakeBlue.rotation.y += 0.007;
      snakeGreen.rotation.x -= 0.002;
      snakeGreen.rotation.y -= 0.005;
      snakeGreen.rotation.z += 0.003;
      renderer.render(scene, camera);
    }}
    function onResize() {{
      camera.aspect = window.innerWidth / window.innerHeight;
      camera.updateProjectionMatrix();
      renderer.setSize(window.innerWidth, window.innerHeight);
    }}
    window.onload = function() {{
      init(); animate();
      window.addEventListener('resize', onResize);
    }};
  </script>
</body>
</html>
"""

components.html(html, height=950, scrolling=False)
