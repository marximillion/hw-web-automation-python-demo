class LandingPage:
    EN = {
        "elements": {
            "resources": {
                "emotional_intelligence": "//a[@title='Emotional Intelligence: Why it’s Important and How to Build it']",
                "anxiety": "//a[@title='Anxiety: Strategies for Coping with Change and Uncertainty']",
                "letting_go": "//a[@title='Letting Go of Expectations']",
                "toolkit": "//a[@class='btn btn-lg btn-primary']",
            },
            "buttons": {
                "sign_in": "//a[@title='Sign in']//i[@class='fa-solid fa-chevron-right font-size-std']"
            }
        },
        "paths": {
            "resources": {
                "emotional_intelligence": "/homewood/neurodiversity-focus-energy-drain-masking",
                "anxiety": "/homewood/emotional-intelligence-why-its-important-how-build",
                "letting_go": "/homewood/ai-anxiety-strategies-coping-with-change-uncertainty",
                "toolkit": "/homewood/navigating-uncertainty-your-mental-health-toolkit",
            },
            "buttons": {
                "sign_in": "/en/login"
            }
        }
    }

    FR = {
        "resources": {
            "emotional_intelligence": "//a[@title='Intelligence émotionnelle : pourquoi elle est importante et comment la développer']",
            "anxiety": "//a[@title='Anxiété : stratégies pour faire face au changement et à l’incertitude']",
            "letting_go": "//a[@title='Lâcher prise des attentes']",
            "toolkit": "//a[@class='btn btn-lg btn-primary']",
        },
        "paths": {
            "emotional_intelligence": "/homewood/neurodiversity-focus-energy-drain-masking",  # adjust if different
            "anxiety": "/homewood/emotional-intelligence-why-its-important-how-build",
            "letting_go": "/homewood/ai-anxiety-strategies-coping-with-change-uncertainty",
            "toolkit": "/homewood/navigating-uncertainty-your-mental-health-toolkit",
        }
    }
