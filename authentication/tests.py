#  <section class="change-background-images">
#     <div class="image-overlay">
#       <div class="image-container">
#         <img src="static/media/images/offices.PNG" alt="Offices">
#       </div>
#       <div class="overlay">
#         <h1>Exotic EPZ Limited Headquarters</h1>
#         <p>Located 1.8 km from Prestige Movers Kenya Limited, next to Government of Nairobi County offices.</p>
#       </div>
#     </div>
#   </section>
  
#   <section class="change-background-images1">
#     <div class="image-overlay">
#       <div class="image-container">
#         <img src="static/media/images/processing.PNG" alt="Processing">
#       </div>
#       <div class="overlay">
#         <h1>Processing of the Nuts</h1>
#         <p>Quality products for healthy and happy living.</p>
#       </div>
#     </div>
#   </section>
  
#   <style>
#     .change-background-images, .change-background-images1 {
#       display: none;
#       height: 80vh;
#     }
  
#     .image-overlay {
#       position: relative;
#       height: 100%;
#     }
  
#     .image-container {
#       position: absolute;
#       top: 0;
#       left: 0;
#       width: 100%;
#       height: 100%;
#       background-size: cover;
#       background-position: center;
#       animation: show-image 0s 2s forwards;
#     }
  
#     .image-container img {
#       width: 100%;
#       height: 100%;
#       object-fit: cover;
#     }
  
#     .overlay {
#         position: absolute;
#         bottom: 0;
#         left: -100%; /* Start offscreen on the left */
#         width: 100%;
#         height: 100px;
#         background-color: rgba(0, 0, 0, 0.5);
#         color: #ff9900;
#         padding: 10px;
#         opacity: 0;
#         animation: show-overlay 2s 2s forwards;
#       }
      
  
#       @keyframes show-overlay {
#         from {
#           left: -100%; /* Start offscreen on the left */
#           opacity: 1;
#         }
#         to {
#           left: 0; /* Move to the left edge of the screen */
#           opacity: 1;
#         }
#       }
      
#   </style>
  
#   <script>
#     var sectionIndex = 0;
#     var sections = document.querySelectorAll('section');
  
#     function showNextSection() {
#       sections[sectionIndex].style.display = 'none';
#       sectionIndex = (sectionIndex + 1) % sections.length;
#       sections[sectionIndex].style.display = 'block';
#     }
  
#     // Show the first section initially
#     sections[sectionIndex].style.display = 'block';
  
#     // Call the showNextSection function every 5 seconds
#     setInterval(showNextSection, 10000);
#   </script>
  






#  <header  class ="fixed-header">
#         <div class="navigations">
#             <div class="nav-brand">
#                 <img src="{% static 'media/images/Capture1.PNG' %}" alt="" id="logo-image">
#             </div>
#             <div class="nav-main">
#                 <nav>
#                     <ul>
#                         <li><a href=""> Home</a></li>
#                         <li><a href=""> About Us</a></li>
#                         <li><a href=""> FAQs</a></li>
#                         <li><a href=""> Partners</a></li>
#                         <li><a href=""> Contact Us</a></li>
#                     </ul>
#                 </nav>
#             </div>
#         </div>
#         <div class="services">
#             <ul>
#                 <li><a href=""><i class="fas fa-seedling text-green"></i>Our Macadamia Nuts</a></li>
#                 <li><a href=""><i class="fas fa-check-circle text-blue"></i>Quality Assurance</a></li>
#                 <li><a href=""><i class="fas fa-globe"></i>Impact</a></li>
#             </ul>
#         </div>
#     </header>