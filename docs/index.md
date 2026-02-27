---
hide:
  - navigation
  - toc
---

# Urbano {.sr-only}

<style>
.md-content__button {
    display: none;
}
.md-button {
  font-size: 16px;
  font-weight: bold;
  padding: 12px 24px;
}
.md-button--primary {
  background-color: #007acc;
  color: white;
}
.center-text {
  text-align: center;
  display: block;
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
  transition: transform 0.3s ease-in-out, border-color 0.3s ease-in-out;
}

.mdx-users__testimonial:hover img {
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
.black-and-white:hover {
    filter: grayscale(0%);
}
</style>

<figure markdown="span">
  ![Urbano Logo](assets/cd/android-chrome-512x512.png){ width="250" .skip-lightbox }
</figure>

<p style="text-align: center; font-size: 24px;">
  Site and mobility analysis in Rhino & Grasshopper. 
</p>

<br>

![Urbano Example Canvas](assets/images/combo.jpg){.skip-lightbox}

<div align="center" markdown>

[:material-rocket-launch: Get Started](https://docs.urbano.io/){ .md-button .md-button--primary }
[:material-download: Download V1](https://www.food4rhino.com/en/app/urbano){ .md-button target="_blank" rel="noopener noreferrer" aria-label="Download V1 (opens in a new tab)" }
[:material-download: Download V2](https://rhinopackages.github.io/?search=urbano&sort=2&p=Urbano2){ .md-button target="_blank" rel="noopener noreferrer" aria-label="Download V2 (opens in a new tab)" }

</div>


---

## 🚀 Features

A preview of what Urbano enables you to do

<div class="grid cards" markdown>

-   ![Screenshot of Download Geospatial Data feature](assets/images/download.png){ width="240" loading=lazy .skip-lightbox .center }

    ---

    __DOWNLOAD GEOSPATIAL DATA__  

    Download maps and points-of-interest data from **OpenStreetMap** directly in Grasshopper.

-   ![Screenshot of Import & Aggregate Data feature](assets/images/import.png){ width="240" loading=lazy .skip-lightbox .center }

    ---

    __IMPORT & AGGREGATE DATA__  

    Parse and merge layers from OSM or shapefiles into a single coherent project model.

-   ![Screenshot of Look-up & Modify Metadata feature](assets/images/metadata.png){ width="240" loading=lazy .skip-lightbox .center }

    ---

    __LOOK-UP & MODIFY METADATA__  

    Attach, query and parametrically edit metadata on any geometric object.

-   ![Screenshot of Build Mobility Model feature](assets/images/build.png){ width="240" loading=lazy .skip-lightbox .center }

    ---

    __BUILD MOBILITY MODEL__  

    Auto-generate a topological street network and building access points ready for simulation.

-   ![Screenshot of Multi-modal Routing feature](assets/images/router.png){ width="240" loading=lazy .skip-lightbox .center }

    ---

    __MULTI-MODAL ROUTING__  

    Compute fastest paths for pedestrians, cyclists or cars between origins and destinations.

-   ![Screenshot of Simulate with Trip Engine feature](assets/images/tripengine.png){ width="240" loading=lazy .skip-lightbox .center }

    ---

    __SIMULATE WITH TRIP ENGINE__  

    Launch activity-based simulations using Amenity Demand Profiles (ADP).

-   ![Screenshot of Analyse Amenities & Streets feature](assets/images/metrics.png){ width="240" loading=lazy .skip-lightbox .center }

    ---

    __ANALYSE AMENITIES & STREETS__  

    Evaluate Streetscore, Amenityscore and Walkscore to assess vitality and accessibility.

-   ![Screenshot of Integrated CAD Workflow feature](assets/images/rhino.png){ width="240" loading=lazy .skip-lightbox .center }

    ---

    __INTEGRATED CAD WORKFLOW__  

    Bake geometry with metadata back to Rhino and visualise results instantly.

</div>

---

## 📊 Metrics

<div class="grid cards" markdown>



-   ![Animated map showing Amenity Demand Profile heatmap](assets/images/adpmetrics.gif){ width="460" loading=lazy  .center }

    ---

    __AMENITY DEMAND PROFILE__  

    Spatiotemporal distribution of human activities; default data provided and fully editable.

-   ![Animated map showing Streetscore metrics on a road network](assets/images/streetmetrics.gif){ width="460" loading=lazy  .center }

    ---

    __STREETSCORE__  

    Counts *Street Hits* to show how many simulated trips use each street segment.

-   ![Animated map showing Amenityscore distribution](assets/images/amenitymetrics.gif){ width="460" loading=lazy  .center }

    ---

    __AMENITYSCORE__  

    Compares amenity demand (Amenity Hits) with supply to reveal over- or under-served areas.

-   ![Animated map showing Walkscore analysis results](assets/images/walkscoremetrics.gif){ width="460" loading=lazy  .center }

    ---

    __WALKSCORE__  

    Calculates a 0-100 walkability rating with customisable weightings.

</div>

---


## 🛠️ Samples

Use cases with Urbano components

<div class="grid cards" markdown>

-   ![GIF demonstrating Urbano Template import workflow](assets/images/Template.gif){ width="500" loading=lazy  .center }

    ---

    __URBANO TEMPLATES__  

    *Import Urbano Template* – starter files that demonstrate each core workflow.

-   ![GIF showing routing calculation for multiple traffic modes](assets/images/Router.gif){ width="500" loading=lazy  .center }

    ---

    __ROUTING__  

    *Router* – compute shortest paths, distances and travel times for multiple traffic modes.

-   ![GIF visualizing reachable buildings within walking distance](assets/images/Walkingdistance.gif){ width="500" loading=lazy  .center }

    ---

    __ACCESSIBILITY WITHIN DISTANCE__  

    *Router* – visualise all buildings reachable from an origin within a chosen threshold.

-   ![GIF demonstrating Trip Engine simulation from origin](assets/images/Basic%20TripEngine.gif){ width="500" loading=lazy  .center }

    ---

    __TRIPS FROM GIVEN ORIGIN__  

    *ADP Trip Engine & Inspect Trip* – split population by ADP and send trips to valid amenities.

-   ![GIF showing Streetscore updates when modifying links](assets/images/Streetscore.gif){ width="500" loading=lazy  .center }

    ---

    __STREETSCORE (ADD LINK)__  

    *ADP Trip Engine & Street Hits* – add or remove links and see Street Hits update instantly.

-   ![GIF showing Amenityscore updates when adding population](assets/images/Amenityscore_addpop.gif){ width="500" loading=lazy  .center }

    ---

    __AMENITYSCORE (ADD POPULATION)__  

    *ADP Trip Engine & Amenity Hits* – add building occupants and observe nearby amenity utilisation.

-   ![GIF showing Amenityscore updates when adding amenities](assets/images/Amenityscore_addamen.gif){ width="500" loading=lazy  .center }

    ---

    __AMENITYSCORE (ADD AMENITIES)__  

    *ADP Trip Engine & Amenity Hits* – insert new amenities to balance supply and demand.

-   ![GIF showing 24-hour time simulation with ADP](assets/images/Time%20Simulation.gif){ width="500" loading=lazy  .center }

    ---

    __AMENITYSCORE (ADP TIME STEPS)__  

    *ADP & Trip Engine* – run 24-hour simulations to capture temporal variations.

-   ![GIF demonstrating Walkscore improvement by adding amenities](assets/images/Walkscore.gif){ width="500" loading=lazy  .center }

    ---

    __WALKSCORE (ADD AMENITIES)__  

    *Trip Engine & Walkscore* – add missing amenities to improve walkability scores.

</div>


---

## 👥 Team


<div class="mdx-users">

<figure class="mdx-users__testimonial black-and-white">
    <img src="assets/images/team/yang.jpg" alt="Yang Yang" loading="lazy" class="skip-lightbox">
    <figcaption class="md-typeset">Yang Yang</figcaption>
  </figure>
  
  <figure class="mdx-users__testimonial black-and-white">
    <img src="assets/images/team/kastner.jpg" alt="Patrick Kastner" loading="lazy" class="skip-lightbox">
    <figcaption class="md-typeset">Patrick Kastner</figcaption>
  </figure>

<figure class="mdx-users__testimonial black-and-white">
    <img src="assets/images/team/dogan.jpg" alt="Timur Dogan" loading="lazy" class="skip-lightbox">
    <figcaption class="md-typeset">Timur Dogan</figcaption>
  </figure>

</div>

## 👥 Alumni & Advisors

<div class="mdx-users">

<figure class="mdx-users__testimonial black-and-white">
    <img src="assets/images/team/saraf.jpg" alt="Nikhil Saraf" loading="lazy" class="skip-lightbox">
    <figcaption class="md-typeset">Nikhil Saraf</figcaption>
  </figure>

<figure class="mdx-users__testimonial black-and-white">
    <img src="assets/images/team/samitha.jpg" alt="Samitha Samaranayake" loading="lazy" class="skip-lightbox">
    <figcaption class="md-typeset">Samitha Samaranayake
</figcaption>
  </figure>

</div>

---

![SysEn](assets/images/logo-systemseng.svg){width="350" .skip-lightbox align=left loading=lazy}  
![ESLAB](assets/images/eslab.svg){width="320" .skip-lightbox align=right loading=lazy}
<center markdown="1">
:octicons-plus-24:
</center>

<br><br><br>

Urbano is being developed as a cross-disciplinary project through a collaboration between the Environmental Systems Lab at Cornell AAP, and the Systems Engineering department at Cornell Engineering.

---

## 🎉 Supporters

<div class="grid" markdown>

![AAP](assets/images/AAP_logo_stacked.png){width="150" .skip-lightbox loading=lazy .center} 
{ .card }

![Cornell](assets/images/cornell.svg){width="125" .skip-lightbox loading=lazy .center} 
{ .card }

![Atkinson](assets/images/atkinson.png){width="325" .skip-lightbox loading=lazy .center}
{ .card }

</div>
