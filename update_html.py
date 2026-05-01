import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Insert About Us below Hero
about_us_html = """  </header>

  <!-- ABOUT US -->
  <section id="about-us" class="py-16 md:py-24 px-6 md:px-12 bg-[#F5F0EB] relative overflow-hidden">
    <div class="max-w-7xl mx-auto flex flex-col md:flex-row items-center gap-16">
      <div class="w-full md:w-[50%] relative reveal-up">
        <div class="relative w-full aspect-[4/5] rounded-3xl overflow-hidden shadow-2xl">
          <img src="https://images.unsplash.com/photo-1618221195710-dd6b41faaea6?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80" alt="About Sagar Associates" class="w-full h-full object-cover hover:scale-105 transition-transform duration-700" />
          <div class="absolute inset-0 bg-primary/10 mix-blend-multiply pointer-events-none"></div>
          <div class="absolute bottom-6 left-6 md:bottom-10 md:left-10 bg-white/90 backdrop-blur-md p-6 rounded-2xl shadow-xl">
             <span class="font-serif text-4xl text-primary">10+</span>
             <p class="text-xs uppercase tracking-widest text-muted font-bold mt-1">Years of Trust</p>
          </div>
        </div>
      </div>
      
      <div class="w-full md:w-[50%] flex flex-col justify-center reveal-up delay-100">
        <span class="text-accent text-xs font-semibold tracking-[0.2em] uppercase mb-4 block inline-flex items-center gap-2">
          <span class="w-8 h-[1px] bg-accent"></span>About Us
        </span>
        <h2 class="font-serif text-4xl md:text-5xl text-primary mb-8 leading-tight">
          Design is easy to see… <br><span class="text-muted/80">but difficult to feel.</span>
        </h2>
        
        <p class="text-muted text-base md:text-lg mb-6 font-light leading-relaxed">
          <span class="font-medium text-primary">And that’s where most designers fail.</span> At Sagar Associates, our approach is different. We observe how you live, how your space flows, how light enters your home — and then we design around you, not just trends.
        </p>
        
        <p class="text-muted text-base md:text-lg mb-6 font-light leading-relaxed">
          Over the years, we have quietly built a reputation as a trusted interior designer in Agra, working on homes that are not only beautiful on day one, but still feel right years later.
        </p>
        
        <p class="text-muted text-base md:text-lg mb-8 font-light leading-relaxed">
          Because in a city like Agra, every home has a different story — and we make sure the design respects that.
        </p>
        
        <div class="bg-primary/5 p-6 rounded-2xl border-l-4 border-accent inline-block reveal-up delay-200 hover:bg-primary/10 transition-colors">
           <p class="text-primary font-medium flex items-center gap-3">
             <span class="text-xl">👉</span> 
             <span>Explore our philosophy as a <a href="/interior-designer-in-agra.html" class="text-accent hover:text-primary transition-colors underline decoration-1 underline-offset-4 font-bold">top interior design firm in Agra</a></span>
           </p>
        </div>
      </div>
    </div>
  </section>

  <!-- SERVICES - BENTO -->"""

content = content.replace("  </header>\n\n  <!-- SERVICES - BENTO -->", about_us_html)

# 2. Comment out 360 VIRTUAL TOUR SECTION
# find from <!-- 360 VIRTUAL TOUR SECTION --> to </section> before <!-- TRANSFORMATION (BEFORE/AFTER) -->
p_360 = re.compile(r'(<!-- 360 VIRTUAL TOUR SECTION -->.*?</section>\n)', re.DOTALL)
m_360 = p_360.search(content)
if m_360:
    block = m_360.group(1)
    block_safe = block.replace("<!--", "<!~~").replace("-->", "~~>")
    content = content.replace(block, "<!-- " + block_safe + " -->\n")

# 3. Comment out TRANSFORMATION (BEFORE/AFTER)
p_trans = re.compile(r'(<!-- TRANSFORMATION \(BEFORE/AFTER\) -->.*?</section>\n)', re.DOTALL)
m_trans = p_trans.search(content)
if m_trans:
    block = m_trans.group(1)
    block_safe = block.replace("<!--", "<!~~").replace("-->", "~~>")
    content = content.replace(block, "<!-- " + block_safe + " -->\n")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Done")
