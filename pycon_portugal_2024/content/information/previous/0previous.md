layout: simple

## Previous Editions

<!-- Previous Editions -->
<a href="https://2022.pycon.pt"><img src="/static/images/icons/porto2022.png" alt="2022 Porto" class="img-fluid main-img"></a>

<div class="container">
    <div class="grid-layout">
        <img src="/static/images/icons/day.png" alt="1 Day" class="img-fluid icon-img">
        <img src="/static/images/icons/attendees.png" alt="141 Attendes" class="img-fluid icon-img">
        <img src="/static/images/icons/portuguese.png" alt="32% Portuguese Attendees, 27 Countries" class="img-fluid icon-img">
        <img src="/static/images/icons/keynote.png" alt="1 Keynote Speaker" class="img-fluid icon-img">
        <img src="/static/images/icons/17.png" alt="17 Speakers" class="img-fluid icon-img">
        <img src="/static/images/icons/109.png" alt="109 Submissions" class="img-fluid icon-img">
        <img src="/static/images/icons/grants.png" alt="3K grants" class="img-fluid icon-img">
        <img src="/static/images/icons/09.png" alt="9 talks" class="img-fluid icon-img">
        <img src="/static/images/icons/05.png" alt="5 workshops" class="img-fluid icon-img">
        <img src="/static/images/icons/lightalks.png" alt="5 lightning talks" class="img-fluid icon-img">
    </div>
</div>

<hr class="purple-line">

<!-- Coimbra -->
<a href="https://2022.pycon.pt"><img src="/static/images/icons/coimbra.png" alt="2023 Coimbra" class="img-fluid main-img"></a>

<div class="container">
    <div class="grid-layout">
        <img src="/static/images/icons/day3.png" alt="3 Days" class="img-fluid icon-img">
        <img src="/static/images/icons/c_attendees.png" alt="153 Attendees" class="img-fluid icon-img">
        <img src="/static/images/icons/c_percentage.png" alt="37.5% Portuguese Attendees, 27 Countries" class="img-fluid icon-img">
        <img src="/static/images/icons/c_keynote.png" alt="2 Keynote speakers" class="img-fluid icon-img">
        <img src="/static/images/icons/c_speakers.png" alt="34 Speakers" class="img-fluid icon-img">
        <img src="/static/images/icons/c_submission.png" alt="122 Submissions" class="img-fluid icon-img">
        <img src="/static/images/icons/c_grant.png" alt="9K Grants" class="img-fluid icon-img">
        <img src="/static/images/icons/c_talks.png" alt="20 Talks" class="img-fluid icon-img">
        <img src="/static/images/icons/c_workshops.png" alt="8 Workshops" class="img-fluid icon-img">
        <img src="/static/images/icons/c_lightalks.png" alt="10 Ligthning Talks" class="img-fluid icon-img">
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
