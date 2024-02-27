def links(request):
    return {
        "home": "/home/",
        "site_menu": {
            "Talks": {
                "dropdown": "true",
                "submenu": {
                    "CALL FOR PARTICIPATION": "/talks/cfp/",
                    "SELECTION PROCESS": "/talks/selection_process/",
                    "SCHEDULE": "/talks/schedule/",
                },
            },
            "Information": {
                "dropdown": "false",
                "href": "/information/",
            },
            "Sponsors/Jobs": {
                "dropdown": "true",
                "submenu": {
                    "SPONSORS": "/sponsors/sponsors",
                    "JOBS": "/sponsors/jobs/",
                    "SPONSORSHIP": "/sponsors/sponsorship/",
                },
            },
            "Logo": {},
            "Conduct": {
                "dropdown": "true",
                "submenu": {
                    "CODE OF CONDUCT": "/conduct/code_of_conduct/",
                    "RESPONSE GUIDE": "/conduct/response_guide/",
                    "PRIVACY GUIDE": "/conduct/privacy_guide/",
                },
            },
            "Tickets": {
                "dropdown": "false",
                "href": "/tickets/",
            },
            "About": {
                "dropdown": "true",
                "submenu": {
                    "CONTACT": "/about/contact/",
                    "CREDITS": "/about/credits/",
                },
            },
        },
        "social_media": {
            "twitter": "https://twitter.com/PyConPT",
            "slack": "https://join.slack.com/t/pyconportugal/shared_invite/zt-1ckszg1ye-QDgxx3lOkC15Ocal8xhCSg",
            "youtube": "https://www.youtube.com/@DisjoinedTech94",
            "linkedin": "https://www.linkedin.com/company/84778227",
            "github": "https://github.com/pyconpt/",
        },
    }
