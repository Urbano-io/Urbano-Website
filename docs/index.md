---
hide:
  - navigation
  - toc
---

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
/* find better solution for this later */
.md-typeset h1 {
position: absolute;
left: -999px;
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
  pointer-events: none; /* Disables mouse clicks and other pointer interactions */
}

.mdx-users__testimonial img {
  border-radius: 50%;       /* Makes images circular */
  border: 3px solid #ddd;
  width: 150px;
  height: 150px;
  pointer-events: none; /* Disables mouse clicks and other pointer interactions */
}
.center {
    display: block;
    margin: 0 auto;
}
.black-and-white {
   filter: grayscale(100%);
   /* Optionally add vendor prefixes for older browser support */
   /* -webkit-filter: grayscale(100%); */
}
</style>

<figure markdown="span">
  ![Urbano Logo](assets/cd/logo.svg){ width="250" .skip-lightbox }
</figure>

<p style="text-align: center; font-size: 24px;">
  Mobility modelling and simulation in Rhino & Grasshopper
</p>

<br>

![Urbano Example Canvas](assets/images/combo.jpg){.skip-lightbox}

<div align="center">
  <a href="https://docs.urbano.io/" class="md-button md-button--primary">Get Started</a>
  <a href="https://www.food4rhino.com/en/app/urbano" class="md-button">Download</a>
</div>


---

## 🚀 Features

A preview of what Urbano enables you to do

<div class="grid cards" markdown>

-   ![](assets/images/download.png){ width="240" loading=lazy .skip-lightbox .center }

    ---

    __DOWNLOAD GEOSPATIAL DATA__  

    Download maps and points-of-interest data from **OpenStreetMap** directly in Grasshopper.

-   ![](assets/images/import.png){ width="240" loading=lazy .skip-lightbox .center }

    ---

    __IMPORT & AGGREGATE DATA__  

    Parse and merge layers from OSM or shapefiles into a single coherent project model.

-   ![](assets/images/metadata.png){ width="240" loading=lazy .skip-lightbox .center }

    ---

    __LOOK-UP & MODIFY METADATA__  

    Attach, query and parametrically edit metadata on any geometric object.

-   ![](assets/images/build.png){ width="240" loading=lazy .skip-lightbox .center }

    ---

    __BUILD MOBILITY MODEL__  

    Auto-generate a topological street network and building access points ready for simulation.

-   ![](assets/images/router.png){ width="240" loading=lazy .skip-lightbox .center }

    ---

    __MULTI-MODAL ROUTING__  

    Compute fastest paths for pedestrians, cyclists or cars between origins and destinations.

-   ![](assets/images/tripengine.png){ width="240" loading=lazy .skip-lightbox .center }

    ---

    __SIMULATE WITH TRIP ENGINE__  

    Launch activity-based simulations using Amenity Demand Profiles (ADP).

-   ![](assets/images/metrics.png){ width="240" loading=lazy .skip-lightbox .center }

    ---

    __ANALYSE AMENITIES & STREETS__  

    Evaluate Streetscore, Amenityscore and Walkscore to assess vitality and accessibility.

-   ![](assets/images/rhino.png){ width="240" loading=lazy .skip-lightbox .center }

    ---

    __INTEGRATED CAD WORKFLOW__  

    Bake geometry with metadata back to Rhino and visualise results instantly.

</div>

---

## 📊 Metrics

<div class="grid cards" markdown>

-   ![](assets/images/adpmetrics.gif){ width="260" loading=lazy .skip-lightbox .center }

    ---

    __AMENITY DEMAND PROFILE__  

    Spatiotemporal distribution of human activities; default data provided and fully editable.

-   ![](assets/images/streetmetrics.gif){ width="260" loading=lazy .skip-lightbox .center }

    ---

    __STREETSCORE__  

    Counts *Street Hits* to show how many simulated trips use each street segment.

-   ![](assets/images/amenitymetrics.gif){ width="260" loading=lazy .skip-lightbox .center }

    ---

    __AMENITYSCORE__  

    Compares amenity demand (Amenity Hits) with supply to reveal over- or under-served areas.

-   ![](assets/images/walkscoremetrics.gif){ width="260" loading=lazy .skip-lightbox .center }

    ---

    __WALKSCORE__  

    Calculates a 0-100 walkability rating with customisable weightings.

</div>

---

## 🛠️ Samples

Use cases with Urbano components

<div class="grid cards" markdown>

-   ![](assets/images/Template.gif){ width="300" loading=lazy .skip-lightbox .center }

    ---

    __URBANO TEMPLATES__  

    *Import Urbano Template* – starter files that demonstrate each core workflow.

-   ![](assets/images/Router.gif){ width="300" loading=lazy .skip-lightbox .center }

    ---

    __ROUTING__  

    *Router* – compute shortest paths, distances and travel times for multiple traffic modes.

-   ![](assets/images/Walkingdistance.gif){ width="300" loading=lazy .skip-lightbox .center }

    ---

    __ACCESSIBILITY WITHIN DISTANCE__  

    *Router* – visualise all buildings reachable from an origin within a chosen threshold.

-   ![](assets/images/Basic%20TripEngine.gif){ width="300" loading=lazy .skip-lightbox .center }

    ---

    __TRIPS FROM GIVEN ORIGIN__  

    *ADP Trip Engine & Inspect Trip* – split population by ADP and send trips to valid amenities.

-   ![](assets/images/Streetscore.gif){ width="300" loading=lazy .skip-lightbox .center }

    ---

    __STREETSCORE (ADD LINK)__  

    *ADP Trip Engine & Street Hits* – add or remove links and see Street Hits update instantly.

-   ![](assets/images/Amenityscore_addpop.gif){ width="300" loading=lazy .skip-lightbox .center }

    ---

    __AMENITYSCORE (ADD POPULATION)__  

    *ADP Trip Engine & Amenity Hits* – add building occupants and observe nearby amenity utilisation.

-   ![](assets/images/Amenityscore_addamen.gif){ width="300" loading=lazy .skip-lightbox .center }

    ---

    __AMENITYSCORE (ADD AMENITIES)__  

    *ADP Trip Engine & Amenity Hits* – insert new amenities to balance supply and demand.

-   ![](assets/images/Time%20Simulation.gif){ width="300" loading=lazy .skip-lightbox .center }

    ---

    __AMENITYSCORE (ADP TIME STEPS)__  

    *ADP & Trip Engine* – run 24-hour simulations to capture temporal variations.

-   ![](assets/images/Walkscore.gif){ width="300" loading=lazy .skip-lightbox .center }

    ---

    __WALKSCORE (ADD AMENITIES)__  

    *Trip Engine & Walkscore* – add missing amenities to improve walkability scores.

</div>


---

## 👥 Team


<div class="mdx-users">

<figure class="mdx-users__testimonial black-and-white">
    <img src="assets/images/team/yang.jpg" alt="Yang Yang" loading="lazy">
    <figcaption class="md-typeset">Yang Yang</figcaption>
  </figure>

<figure class="mdx-users__testimonial black-and-white">
    <img src="assets/images/team/dogan.jpg" alt="Timur Dogan" loading="lazy">
    <figcaption class="md-typeset">Timur Dogan</figcaption>
  </figure>

</div>

## 👥 Alumni

<div class="mdx-users">

<figure class="mdx-users__testimonial black-and-white">
    <img src="assets/images/team/saraf.jpg" alt="Nikhil Saraf" loading="lazy">
    <figcaption class="md-typeset">Nikhil Saraf</figcaption>
  </figure>

<figure class="mdx-users__testimonial black-and-white">
    <img src="assets/images/team/samitha.jpg" alt="Samitha Samaranayake" loading="lazy">
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
