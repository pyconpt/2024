layout: simple

## Previous Editions

<!-- Previous Editions -->
<img src="/static/images/icons/porto2022.png" alt="Attendees" class="img-fluid main-img">

<div class="container">
    <div class="grid-layout">
        <img src="/static/images/icons/day.png" alt="Day" class="img-fluid icon-img">
        <img src="/static/images/icons/attendees.png" alt="Attendees" class="img-fluid icon-img">
        <img src="/static/images/icons/portuguese.png" alt="Portuguese" class="img-fluid icon-img">
        <img src="/static/images/icons/keynote.png" alt="Keynote" class="img-fluid icon-img">
        <img src="/static/images/icons/17.png" alt="Day" class="img-fluid icon-img">
        <img src="/static/images/icons/109.png" alt="Day" class="img-fluid icon-img">
        <img src="/static/images/icons/grants.png" alt="Day" class="img-fluid icon-img">
        <img src="/static/images/icons/09.png" alt="Day" class="img-fluid icon-img">
        <img src="/static/images/icons/05.png" alt="Day" class="img-fluid icon-img">
        <img src="/static/images/icons/lightalks.png" alt="Day" class="img-fluid icon-img">
    </div>
</div>

<hr class="purple-line">

<!-- Coimbra -->
<img src="/static/images/icons/coimbra.png" alt="Attendees" class="img-fluid main-img">

<div class="container">
    <div class="grid-layout">
        <img src="/static/images/icons/day3.png" alt="Day" class="img-fluid icon-img">
        <img src="/static/images/icons/c_attendees.png" alt="Attendees" class="img-fluid icon-img">
        <img src="/static/images/icons/c_percentage.png" alt="Portuguese" class="img-fluid icon-img">
        <img src="/static/images/icons/c_keynote.png" alt="Keynote" class="img-fluid icon-img">
        <img src="/static/images/icons/c_speakers.png" alt="Day" class="img-fluid icon-img">
        <img src="/static/images/icons/c_submission.png" alt="Day" class="img-fluid icon-img">
        <img src="/static/images/icons/c_grant.png" alt="Day" class="img-fluid icon-img">
        <img src="/static/images/icons/c_talks.png" alt="Day" class="img-fluid icon-img">
        <img src="/static/images/icons/c_workshops.png" alt="Day" class="img-fluid icon-img">
        <img src="/static/images/icons/c_lightalks.png" alt="Day" class="img-fluid icon-img">
    </div>
</div>

<style>
.main-img {
    max-width: 60%;
    margin-bottom: 20px;
}

.container {
    padding: 20px 0;
}

.grid-layout {
    display: grid;
    grid-template-columns: repeat(5, 1fr); /* 5 columns */
    gap: 20px; /* Space between images */
}

.icon-img {
    width: 60%; /* Use full width of the grid cell */
    height: auto;
    max-width: 100%; /* Responsive to container */
    margin: 0; /* No extra margins */
}

/* Responsive Design for Smaller Screens */
@media (max-width: 1024px) {
    .grid-layout {
        grid-template-columns: repeat(5, 1fr); /* 5 columns for tablets and larger screens */
    }

    .icon-img {
    width: 90%; /* Use full width of the grid cell */
    height: auto;
    max-width: 100%; /* Responsive to container */
    margin: 0; /* No extra margins */
}

}

@media (max-width: 768px) {
    .grid-layout {
        grid-template-columns: repeat(auto-fit, minmax(120px, 1fr)); /* Flexible columns for mobile */
    }
    .icon-img {
    width: 90%; /* Use full width of the grid cell */
    height: auto;
    max-width: 100%; /* Responsive to container */
    margin: 0; /* No extra margins */
}


}

@media (max-width: 600px) {
    .grid-layout {
        grid-template-columns: repeat(auto-fit, minmax(90px, 1fr)); /* Smaller columns for very small screens */
    }
    .icon-img {
    width: 90%; /* Use full width of the grid cell */
    height: auto;
    max-width: 100%; /* Responsive to container */
    margin: 0; /* No extra margins */
}

}

</style>
