---
hide:
  - navigation
  - toc
---

<!-- @Jules @palette: Please do not add a title/heading back to this landing page. -->

<style>
.md-content h1 {
    display: none !important;
}
.md-content__button {
    display: none;
}
.md-button {
  font-size: 16px;
  font-weight: bold;
  padding: 12px 24px;
  transition: all 0.2s ease-in-out;
}
.md-button:hover,
.md-button:focus-visible {
  transform: translateY(-2px);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
}
.md-button:focus-visible {
  outline: 2px solid #007acc;
  outline-offset: 4px;
}
.md-button:active {
  transform: translateY(0) scale(0.98);
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
.md-button--primary {
  background-color: #007acc;
  color: white;
}
.md-button--primary:hover,
.md-button--primary:focus-visible {
  background-color: #005f9e;
}
.center-text {
  text-align: center;
  display: block;
}

@media (prefers-reduced-motion: reduce) {
  .md-button,
  .md-button:hover,
  .md-button:focus-visible,
  .md-button:active,
  .mdx-users__testimonial img {
    transition: none !important;
    transform: none !important;
  }
}

.mdx-users {
  display: flex;
  justify-content: center;  /* Centers items horizontally */
  flex-wrap: wrap;          /* Ensures they wrap on smaller screens */
  gap: 40px;                /* Adds spacing between items */
}

.mdx-users__testimonial {
  text-align: center;
  max-width: 220px;         /* Limits width so they stay aligned */
}

.mdx-users__testimonial img {
  border-radius: 50%;       /* Makes images circular */
  border: 3px solid #ddd;
  width: 150px;
  height: 150px;
  object-fit: cover;        /* Prevents image distortion */
  transition: transform 0.3s ease-in-out, border-color 0.3s ease-in-out;
}

.mdx-users__testimonial:hover img,
.mdx-users__testimonial:focus-visible img {
    transform: scale(1.05);
    border-color: #007acc;
}

.center {
    display: block;
    margin: 0 auto;
}
.black-and-white {
   filter: grayscale(100%);
   transition: filter 0.3s ease-in-out;
   /* Optionally add vendor prefixes for older browser support */
   /* -webkit-filter: grayscale(100%); */
}
.black-and-white:hover,
.black-and-white:focus-visible {
    filter: grayscale(0%);
}
.black-and-white:focus-visible {
    outline: 2px solid #007acc;
    outline-offset: 4px;
    border-radius: 8px;
}
</style>

<div class="workflow-teaser workflow-teaser--hero">
  <video autoplay loop muted playsinline controls preload="metadata" aria-label="Urbano workflow teaser video">
    <source src="assets/videos/Urbano2-WorkflowTeaser1.mp4" type="video/mp4">
    Your browser does not support embedded videos. You can
    <a href="assets/videos/Urbano2-WorkflowTeaser1.mp4">download the teaser video here</a>.
  </video>
</div>

<div style="display: flex; justify-content: center; align-items: center; flex-wrap: wrap; gap: 1rem;" markdown>

[:material-rocket-launch: Get Started](https://docs.urbano.io/){ .md-button .md-button--primary target="_blank" rel="noopener noreferrer" aria-label="Get Started (opens in a new tab)" }
[:material-download: Download](https://rhinopackages.github.io/?search=urbano&sort=2&p=Urbano2){ .md-button target="_blank" rel="noopener noreferrer" aria-label="Download (opens in a new tab)" }

</div>


---

## <span aria-hidden="true">👥</span> Team


<div class="mdx-users">

<figure class="mdx-users__testimonial black-and-white" tabindex="0" role="group" aria-label="Team member: Yang Yang">
    <img src="assets/images/team/yang.jpg" alt="" loading="lazy" class="skip-lightbox">
    <figcaption class="md-typeset">Yang Yang</figcaption>
  </figure>
  
  <figure class="mdx-users__testimonial black-and-white" tabindex="0" role="group" aria-label="Team member: Patrick Kastner">
    <img src="assets/images/team/kastner.jpg" alt="" loading="lazy" class="skip-lightbox">
    <figcaption class="md-typeset">Patrick Kastner</figcaption>
  </figure>

<figure class="mdx-users__testimonial black-and-white" tabindex="0" role="group" aria-label="Team member: Timur Dogan">
    <img src="assets/images/team/dogan.jpg" alt="" loading="lazy" class="skip-lightbox">
    <figcaption class="md-typeset">Timur Dogan</figcaption>
  </figure>

</div>

## <span aria-hidden="true">👥</span> Alumni & Advisors

<div class="mdx-users">

<figure class="mdx-users__testimonial black-and-white" tabindex="0" role="group" aria-label="Alumni and Advisor: Nikhil Saraf">
    <img src="assets/images/team/saraf.jpg" alt="" loading="lazy" class="skip-lightbox">
    <figcaption class="md-typeset">Nikhil Saraf</figcaption>
  </figure>

<figure class="mdx-users__testimonial black-and-white" tabindex="0" role="group" aria-label="Alumni and Advisor: Samitha Samaranayake">
    <img src="assets/images/team/samitha.jpg" alt="" loading="lazy" class="skip-lightbox">
    <figcaption class="md-typeset">Samitha Samaranayake
</figcaption>
  </figure>

</div>

---

<div style="display: flex; justify-content: center; align-items: center; flex-wrap: wrap; gap: 2rem; margin: 3rem 0;" markdown>

![Cornell Systems Engineering](assets/images/logo-systemseng.svg){width="350" .skip-lightbox loading=lazy}
<span aria-hidden="true">:octicons-plus-24:</span>
![Environmental Systems Lab](assets/images/eslab.svg){width="320" .skip-lightbox loading=lazy}

</div>

Urbano is being developed as a cross-disciplinary project through a collaboration between the Environmental Systems Lab at Cornell AAP, and the Systems Engineering department at Cornell Engineering.

---

## <span aria-hidden="true">🎉</span> Supporters




<div class="grid" markdown>

[![AAP](assets/images/AAP_logo_stacked.png){width="150" .skip-lightbox loading=lazy .center alt=""}](https://aap.cornell.edu/){ .card target="_blank" rel="noopener noreferrer" aria-label="Cornell AAP (opens in a new tab)" }

[![Cornell](assets/images/cornell.svg){width="125" .skip-lightbox loading=lazy .center alt=""}](https://www.cornell.edu/){ .card target="_blank" rel="noopener noreferrer" aria-label="Cornell University (opens in a new tab)" }

[![Atkinson](assets/images/atkinson.png){width="325" .skip-lightbox loading=lazy .center alt=""}](https://atkinson.cornell.edu/){ .card target="_blank" rel="noopener noreferrer" aria-label="Cornell Atkinson Center for Sustainability (opens in a new tab)" }

</div>
