from logging import error
from flask import Flask, request
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

null = None

class Home(Resource):
    def get(seft):
        return {
            "data": [
                {
                    "headers": [
                        {
                            "top": [
                                {
                                    "left": [
                                        {
                                            "text": "+880166 253 232",
                                            "url": "null"
                                        },
                                        {
                                            "text": "info@domain.com",
                                            "url": "null"
                                        }
                                    ]
                                },
                                {
                                    "right": {
                                        "text": "Mon - Fri: 9:00 - 19:00 / Closed on Weekends",
                                        "url": "null"
                                    }
                                }
                            ]
                        },
                        {
                            "down": [
                                {
                                    "left": {
                                        "image": "inds",
                                        "url": "data:image/webp;base64,UklGRnwBAABXRUJQVlA4TG8BAAAvXkAHELdAkG1TiuPd3+O5w8gLBJLI9ueYhECAwhYX+D9JEyQUHQAUgZFe4DAwyJJtJRKkVz1qToqA+9+rgJbZ419E/yegdB37g52fRmMr2DCRzVslsvMO+t+sHOMF4OnCrHminJ25H2VFzSrMoudnkZ0Lk5sindw+dTMFpezAFBWnMC20Ek3mDSazxbQs03TfjOpw0bJKC+/N8tDWZU/V6zuoNo8BFPJFeUKdG6hq5c9rFQA7DcDp3QByTBypAGoppVR83gMAj0MAuiMYY8kh4nRh4SKYIXayIaEnMLZU3nUbOQSJEVH/1YBniN90GWkCR5ug/gJxstFmgKe3EL0gOTxUmhtvDVzA1y/mj11OhzIAiZ19PACgehnfP+yvu1SPqFEwA5Xs9gDFO/cDB8IZgEPUGvnlBfc69aKMF0CWoS0or4BGJAad4YLQ4fSBLbHEahauZrUDbN0GHm0BuTF+c35i7zv1q2Ltk3s/7oJ5AA=="
                                    }
                                },
                                {
                                    "right": [
                                        {
                                            "menubar": [
                                                {
                                                    "text": "Home",
                                                    "url": "https://preview.colorlib.com/theme/inds/index.html"
                                                },
                                                {
                                                    "text": "About",
                                                    "url": "https://preview.colorlib.com/theme/inds/about.html"
                                                },
                                                {
                                                    "text": "Industries",
                                                    "url": "https://preview.colorlib.com/theme/inds/industries.html"
                                                },
                                                {
                                                    "text": "Works",
                                                    "url": "https://preview.colorlib.com/theme/inds/work.html"
                                                },
                                                {
                                                    "text": "Blog",
                                                    "url": "https://preview.colorlib.com/theme/inds/blog.html",
                                                    "dropdown": [
                                                        {
                                                            "text": "Blog",
                                                            "url": "https://preview.colorlib.com/theme/inds/blog.html"
                                                        },
                                                        {
                                                            "text": "blog details",
                                                            "url": "https://preview.colorlib.com/theme/inds/single-blog.html"
                                                        }
                                                    ]
                                                },
                                                {
                                                    "text": "Pages",
                                                    "url": "https://preview.colorlib.com/theme/inds/contact.html#",
                                                    "Text_pages": [
                                                        {
                                                            "text": "Contact",
                                                            "url": "https://preview.colorlib.com/theme/inds/contact.html"
                                                        },
                                                        {
                                                            "text": "Element",
                                                            "url": "https://preview.colorlib.com/theme/inds/elements.html"
                                                        }
                                                    ]
                                                },
                                            ]
                                        },
                                        {
                                            "specialmenubar": [
                                                {
                                                    "text": "Get a quote",
                                                    "url": "https://preview.colorlib.com/theme/inds/contact.html#"
                                                }
                                            ]
                                        }
                                    ]
                                }
                            ]
                        }
                    ],
                    "Body": [
                        {
                            "banner": [
                                {
                                    "image": "gambar industry",
                                    "url": "null"
                                },
                                {
                                    "box": [
                                        {
                                            "text": "industery solutions!",
                                            "url": "null"
                                        },
                                        {
                                            "text": "lorem ipsum dolor sit amet",
                                            "url": "null"
                                        },
                                        {
                                            "button_click": [
                                                {
                                                    "text": "our service",
                                                    "url": "null"
                                                }
                                            ]
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            "main-content": [
                                {
                                    "content1": [
                                        {
                                            "group1": [
                                                {
                                                    "image": "automotive",
                                                    "text": "Automotive Manufacturing",
                                                    "text2": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore.",
                                                    "image2": "arrow",
                                                    "url": "https://preview.colorlib.com/theme/inds/industries.html"
                                                }
                                            ]
                                        },
                                        {
                                            "group2": [
                                                {
                                                    "image": "market",
                                                    "text": "Heavy industry market",
                                                    "text2": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore.",
                                                    "image2": "arrow",
                                                    "url": "https://preview.colorlib.com/theme/inds/industries.html"
                                                }
                                            ]
                                        },
                                        {
                                            "group3": [
                                                {
                                                    "image": "analyst",
                                                    "text": "ndustry analysis",
                                                    "text2": " Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore.",
                                                    "image2": "arrow",
                                                    "url": "https://preview.colorlib.com/theme/inds/industries.html"
                                                }
                                            ]
                                        }
                                    ]
                                },
                                {
                                    "content2": [
                                        {
                                            "left": [
                                                {
                                                    "text": "Safe IndusterySolutions That Saves our Valuable Time and mony!",
                                                    "text2": "Logisti Group is a representative logistics operator providing full range of service in the sphere of customs clearance and transportation worldwide for any type of cargo.",
                                                    "text3": "Lorem ipsum dolor sit amet, consectetur ipis adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna oris aliqua. Ut enim ad minim veniam, quis nostrud.exercitation ullamco laboris nisi ut aliquip ex ea commodo nsequat. Duis aute irure dolor in repr.",
                                                    "button_click": [
                                                        {
                                                            "text4": "our service",
                                                            "url": "https://preview.colorlib.com/theme/inds/industries.html"
                                                        }
                                                    ]
                                                }
                                            ]
                                        },
                                        {
                                            "right": [
                                                {
                                                    "image": "gambar karyawan",
                                                    "icon": "globe",
                                                    "box": [
                                                        {
                                                            "text": "Our Mission",
                                                            "text2": "Quis ipsum suspendisse ultrices gravidae Risus commodo."
                                                        }
                                                    ]
                                                }
                                            ]
                                        }
                                    ]
                                },
                                {
                                    "content3": [
                                        {
                                            "group1": [
                                                {
                                                    "image": "gambar orang bekerja",
                                                    "text": "01. floride chemical factory ",
                                                    "hover": [
                                                        {
                                                            "text": "01. Floride Chemicals Factory Lorem ipsum dolor sit amet, consectetur smo adipiscing elit, sed do eiusmod tempor inciut labore et dolore magna ali.",
                                                            "text2": "read more",
                                                            "url": "https://preview.colorlib.com/theme/inds/work.html"
                                                        }
                                                    ]
                                                }
                                            ]
                                        },
                                        {
                                            "group2": [
                                                {
                                                    "image": "gambar bangunan pabrik",
                                                    "text": "02. floride chemical factory ",
                                                    "hover": [
                                                        {
                                                            "text": "01. Floride Chemicals Factory Lorem ipsum dolor sit amet, consectetur smo adipiscing elit, sed do eiusmod tempor inciut labore et dolore magna ali.",
                                                            "text2": "read more",
                                                            "url": "https://preview.colorlib.com/theme/inds/work.html"
                                                        }
                                                    ]
                                                }
                                            ]
                                        },
                                        {
                                            "group3": [
                                                {
                                                    "image": "gambar orang bekerja",
                                                    "text": "03. floride chemical factory ",
                                                    "hover": [
                                                        {
                                                            "text": "01. Floride Chemicals Factory Lorem ipsum dolor sit amet, consectetur smo adipiscing elit, sed do eiusmod tempor inciut labore et dolore magna ali.",
                                                            "text2": "read more",
                                                            "url": "https://preview.colorlib.com/theme/inds/work.html"
                                                        }
                                                    ]
                                                }
                                            ]
                                        },
                                        {
                                            "group4": [
                                                {
                                                    "image": "gambar orang bekerja",
                                                    "text": "04. floride chemical factory ",
                                                    "hover": [
                                                        {
                                                            "text": "01. Floride Chemicals Factory Lorem ipsum dolor sit amet, consectetur smo adipiscing elit, sed do eiusmod tempor inciut labore et dolore magna ali.",
                                                            "text2": "read more",
                                                            "url": "https://preview.colorlib.com/theme/inds/work.html"
                                                        }
                                                    ]
                                                }
                                            ]
                                        }
                                    ]
                                },
                                {
                                    "content4": [
                                        {
                                            "group1": [
                                                {
                                                    "text": "Our Team Best Mambers",
                                                    "text2": "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna ua. Ut enim ad minim veni.",
                                                    "button_click": [
                                                        {
                                                            "text3": "contact us",
                                                            "url": "https://preview.colorlib.com/theme/inds/contact.html"
                                                        }
                                                    ]
                                                }
                                            ]
                                        },
                                        {
                                            "group2": [
                                                {
                                                    "image": "gambar karyawan",
                                                    "text1": "bruce roberts.",
                                                    "text2": "team officer"
                                                }
                                            ]
                                        },
                                        {
                                            "group3": [
                                                {
                                                    "image": "gambar karyawan",
                                                    "text1": "bruce roberts.",
                                                    "text2": "team officer"
                                                }
                                            ]
                                        },
                                        {
                                            "group4": [
                                                {
                                                    "image": "gambar karyawan",
                                                    "text1": "bruce roberts.",
                                                    "text2": "team officer"
                                                }
                                            ]
                                        },
                                        {
                                            "group5": [
                                                {
                                                    "image": "gambar karyawan",
                                                    "text1": "bruce roberts.",
                                                    "text2": "team officer"
                                                }
                                            ]
                                        },
                                        {
                                            "group6": [
                                                {
                                                    "image": "gambar karyawan",
                                                    "text1": "bruce roberts.",
                                                    "text2": "team officer"
                                                }
                                            ]
                                        }
                                    ]
                                },
                                {
                                    "content5": [
                                        {
                                            "text": "logisti group is a representative logistic operator providing full rangen of ser of customs clearance and transportation worl.",
                                            "text2": "jesya inn - co founder",
                                            "image": "profil"
                                        }
                                    ]
                                },
                                {
                                    "content6": [
                                        {
                                            "group1": [
                                                {
                                                    "image": "gambar orang bekerja",
                                                    "text": "November 24, 2020 | Manufacturing",
                                                    "text2": "david droga still has faith adversting dorga",
                                                    "url": "https://preview.colorlib.com/theme/inds/single-blog.html",
                                                    "text3": "Read more",
                                                    "url2": "https://preview.colorlib.com/theme/inds/single-blog.html"
                                                }
                                            ]
                                        },
                                        {
                                            "group2": [
                                                {
                                                    "image": "gambar orang bekerja",
                                                    "text": "November 24, 2020 | Manufacturing",
                                                    "text2": "david droga still has faith adversting dorga",
                                                    "url": "https://preview.colorlib.com/theme/inds/single-blog.html",
                                                    "text3": "Read more",
                                                    "url2": "https://preview.colorlib.com/theme/inds/single-blog.html"
                                                }
                                            ]
                                        }
                                    ]
                                }
                            ]
                        }
                    ],
                    "footers": [
                        {
                            "top": [
                                {
                                    "left": {
                                        "text": "Want To WorkWith Us? Hit The Button.",
                                        "url": "null"
                                    }
                                },
                                {
                                    "right": {
                                        "button_click": [
                                            {
                                                "text": "Lets work togther",
                                                "url": "https://preview.colorlib.com/theme/inds/#"
                                            }
                                        ]
                                    }
                                }
                            ]
                        },
                        {
                            "down": [
                                {
                                    "top": [
                                        {
                                            "left": [
                                                {
                                                    "text": "ABOUT US",
                                                    "url": "null"
                                                },
                                                {
                                                    "text": "Heaven fruitful doesn't over",
                                                    "url": "null"
                                                },
                                                {
                                                    "text": "lesser days appear creeping",
                                                    "url": "null"
                                                },
                                                {
                                                    "text": "seasons so behold bearing",
                                                    "url": "null"
                                                },
                                                {
                                                    "image": "inds",
                                                    "url": "https://preview.colorlib.com/theme/inds/assets/img/logo/xlogo2_footer.png.pagespeed.ic.V-sLseuErK.webp"
                                                },
                                                {
                                                    "text": "CONTACT INFO",
                                                    "url": "null"
                                                },
                                                {
                                                    "text": "Address :Your address goes here",
                                                    "url": "null"
                                                },
                                                {
                                                    "text": "Phone : +8880 44338899",
                                                    "url": "https://preview.colorlib.com/theme/inds/#"
                                                },
                                                {
                                                    "text": "Our Photo Gellary",
                                                    "url": "https://preview.colorlib.com/theme/inds/#"
                                                }
                                            ]
                                        },
                                        {
                                            "right": [
                                                {
                                                    "text": "IMPORTANT LINK",
                                                    "url": "null"
                                                },
                                                {
                                                    "text": "View Project",
                                                    "url": "https://preview.colorlib.com/theme/inds/#"
                                                },
                                                {
                                                    "text": "Contact Us",
                                                    "url": "https://preview.colorlib.com/theme/inds/#"
                                                },
                                                {
                                                    "text": "Testimonial",
                                                    "url": "https://preview.colorlib.com/theme/inds/#"
                                                },
                                                {
                                                    "text": "Proparties",
                                                    "url": "https://preview.colorlib.com/theme/inds/#"
                                                },
                                                {
                                                    "text": "Support",
                                                    "url": "https://preview.colorlib.com/theme/inds/#"
                                                },
                                                {
                                                    "text": "NEWSLETTER",
                                                    "url": "null"
                                                },
                                                {
                                                    "text": "Heaven fruitful doesn't over lesser in",
                                                    "url": "null"
                                                },
                                                {
                                                    "text": "days. Appear creeping seasons",
                                                    "url": "null"
                                                },
                                                {
                                                    "SearchBar": [
                                                        {
                                                            "placeholder": "Email Adress",
                                                            "defaultValue": "null",
                                                            "icon": "send",
                                                            "url": "https://preview.colorlib.com/theme/inds/assets/img/icon/xform_icon.png.pagespeed.ic.myHEUnsh8f.webp"
                                                        }
                                                    ]
                                                }
                                            ]
                                        }
                                    ]
                                },
                                {
                                    "down": [
                                        {
                                            "left": [
                                                {
                                                    "text": "Copyright ©2022 All rights reserved",
                                                    "url": "null"
                                                },
                                                {
                                                    "text": "This template is made with  ",
                                                    "url": "null"
                                                },
                                                {
                                                    "icon": "love",
                                                    "url": "null"
                                                },
                                                {
                                                    "text": "by Colorlib",
                                                    "url": "https://colorlib.com/"
                                                }
                                            ]
                                        },
                                        {
                                            "right": [
                                                {
                                                    "icon": "facebook",
                                                    "url": "null"
                                                },
                                                {
                                                    "icon": "Twitter",
                                                    "url": "null"
                                                },
                                                {
                                                    "icon": "Globe",
                                                    "url": "null"
                                                },
                                                {
                                                    "icon": "Be",
                                                    "url": "null"
                                                },
                                                {
                                                    "icon": "arrow",
                                                    "url": "https://preview.colorlib.com/theme/inds/#top"
                                                }
                                            ]
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                }
            ]
        }

class About_Us(Resource):
    def get(seft):
        return {
            "data": [
                {
                    "banner": [
                        {
                            "image": "backgrond warna biru",
                            "text": "about us"
                        }
                    ],
                    "content1": [
                        {
                            "left": [
                                {
                                    "text": "Safe IndusterySolutions That Saves our Valuable Time and mony!",
                                    "text2": "Logisti Group is a representative logistics operator providing full range of service in the sphere of customs clearance and transportation worldwide for any type of cargo.",
                                    "text3": "Lorem ipsum dolor sit amet, consectetur ipis adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna oris aliqua. Ut enim ad minim veniam, quis nostrud.exercitation ullamco laboris nisi ut aliquip ex ea commodo nsequat. Duis aute irure dolor in repr.",
                                    "button_click": [
                                        {
                                            "text4": "our service",
                                            "url": "https://preview.colorlib.com/theme/inds/industries.html"
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            "right": [
                                {
                                    "image": "gambar karyawan",
                                    "icon": "globe",
                                    "box": [
                                        {
                                            "text": "Our Mission",
                                            "text2": "Quis ipsum suspendisse ultrices gravidae Risus commodo."
                                        }
                                    ]
                                }
                            ]
                        }
                    ],
                    "content2": [
                        {
                            "text": "logisti group is a representative logistic operator providing full rangen of ser of customs clearance and transportation worl.",
                            "text2": "jesya inn - co founder",
                            "image": "profil"
                        }
                    ],
                    "content3": [
                        {
                            "profilmembers": [
                                {
                                    "text": "Our Team Best Mambers",
                                    "text2": "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna ua. Ut enim ad minim veni.",
                                    "button_click": [
                                        {
                                            "text3": "contact us",
                                            "url": "https://preview.colorlib.com/theme/inds/contact.html"
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            "members": [
                                {
                                    "image": "gambar karyawan",
                                    "text1": "bruce roberts.",
                                    "text2": "team officer"
                                },
                                {
                                    "image": "gambar karyawan",
                                    "text1": "bruce roberts.",
                                    "text2": "team officer"
                                },
                                {
                                    "image": "gambar karyawan",
                                    "text1": "bruce roberts.",
                                    "text2": "team officer"
                                },
                                {
                                    "image": "gambar karyawan",
                                    "text1": "bruce roberts.",
                                    "text2": "team officer"
                                },
                                {
                                    "image": "gambar karyawan",
                                    "text1": "bruce roberts.",
                                    "text2": "team officer"
                                },
                                {
                                    "image": "gambar karyawan",
                                    "text1": "bruce roberts.",
                                    "text2": "team officer"
                                }
                            ]
                        }
                    ]
                }
            ]
        }

class Service(Resource):
    def get(seft):
        return {
            "data": [
                {
                    "banner": [
                        {
                            "image": "backgrond warna biru",
                            "text": "service"
                        }
                    ],
                    "content": [
                        {
                            "group1": [
                                {
                                    "image": "automotive",
                                    "text": "Automotive Manufacturing",
                                    "text2": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore.",
                                    "image2": "arrow",
                                    "url": "https://preview.colorlib.com/theme/inds/industries.html"
                                }
                            ]
                        },
                        {
                            "group2": [
                                {
                                    "image": "market",
                                    "text": "Heavy industry market",
                                    "text2": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore.",
                                    "image2": "arrow",
                                    "url": "https://preview.colorlib.com/theme/inds/industries.html"
                                }
                            ]
                        },
                        {
                            "group3": [
                                {
                                    "image": "analyst",
                                    "text": "ndustry analysis",
                                    "text2": " Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore.",
                                    "image2": "arrow",
                                    "url": "https://preview.colorlib.com/theme/inds/industries.html"
                                }
                            ]
                        },
                        {
                            "group4": [
                                {
                                    "image": "automotive",
                                    "text": "Automotive Manufacturing",
                                    "text2": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore.",
                                    "image2": "arrow",
                                    "url": "https://preview.colorlib.com/theme/inds/industries.html"
                                }
                            ]
                        },
                        {
                            "group5": [
                                {
                                    "image": "market",
                                    "text": "Heavy industry market",
                                    "text2": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore.",
                                    "image2": "arrow",
                                    "url": "https://preview.colorlib.com/theme/inds/industries.html"
                                }
                            ]
                        },
                        {
                            "group6": [
                                {
                                    "image": "analyst",
                                    "text": "ndustry analysis",
                                    "text2": " Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore.",
                                    "image2": "arrow",
                                    "url": "https://preview.colorlib.com/theme/inds/industries.html"
                                }
                            ]
                        }
                    ]
                }
            ]
        }

class Works(Resource):
    def get(seft):
        return {
            "data": [
                {
                    "banner": [
                        {
                            "image": "backgrond warna biru",
                            "text": "works"
                        }
                    ],
                    "content": [
                        {
                            "group1": [
                                {
                                    "image": "gambar orang bekerja",
                                    "text": "01. floride chemical factory ",
                                    "hover": [
                                        {
                                            "text": "01. Floride Chemicals Factory Lorem ipsum dolor sit amet, consectetur smo adipiscing elit, sed do eiusmod tempor inciut labore et dolore magna ali.",
                                            "text2": "read more",
                                            "url": "https://preview.colorlib.com/theme/inds/work.html"
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            "group2": [
                                {
                                    "image": "gambar bangunan pabrik",
                                    "text": "02. floride chemical factory ",
                                    "hover": [
                                        {
                                            "text": "01. Floride Chemicals Factory Lorem ipsum dolor sit amet, consectetur smo adipiscing elit, sed do eiusmod tempor inciut labore et dolore magna ali.",
                                            "text2": "read more",
                                            "url": "https://preview.colorlib.com/theme/inds/work.html"
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            "group3": [
                                {
                                    "image": "gambar orang bekerja",
                                    "text": "03. floride chemical factory ",
                                    "hover": [
                                        {
                                            "text": "01. Floride Chemicals Factory Lorem ipsum dolor sit amet, consectetur smo adipiscing elit, sed do eiusmod tempor inciut labore et dolore magna ali.",
                                            "text2": "read more",
                                            "url": "https://preview.colorlib.com/theme/inds/work.html"
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            "group4": [
                                {
                                    "image": "gambar orang bekerja",
                                    "text": "04. floride chemical factory ",
                                    "hover": [
                                        {
                                            "text": "01. Floride Chemicals Factory Lorem ipsum dolor sit amet, consectetur smo adipiscing elit, sed do eiusmod tempor inciut labore et dolore magna ali.",
                                            "text2": "read more",
                                            "url": "https://preview.colorlib.com/theme/inds/work.html"
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            "group5": [
                                {
                                    "image": "gambar pusat listrik",
                                    "text": "05. floride chemical factory ",
                                    "hover": [
                                        {
                                            "text": "06. Floride Chemicals Factory Lorem ipsum dolor sit amet, consectetur smo adipiscing elit, sed do eiusmod tempor inciut labore et dolore magna ali.",
                                            "text2": "read more",
                                            "url": "https://preview.colorlib.com/theme/inds/work.html"
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            "group6": [
                                {
                                    "image": "gambar jembatan",
                                    "text": "06. floride chemical factory ",
                                    "hover": [
                                        {
                                            "text": "06. Floride Chemicals Factory Lorem ipsum dolor sit amet, consectetur smo adipiscing elit, sed do eiusmod tempor inciut labore et dolore magna ali.",
                                            "text2": "read more",
                                            "url": "https://preview.colorlib.com/theme/inds/work.html"
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            "group7": [
                                {
                                    "image": "gambar corong asap pabrik",
                                    "text": "07. floride chemical factory ",
                                    "hover": [
                                        {
                                            "text": "07. Floride Chemicals Factory Lorem ipsum dolor sit amet, consectetur smo adipiscing elit, sed do eiusmod tempor inciut labore et dolore magna ali.",
                                            "text2": "read more",
                                            "url": "https://preview.colorlib.com/theme/inds/work.html"
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            "group8": [
                                {
                                    "image": "gambar alat pabrik",
                                    "text": "08. floride chemical factory ",
                                    "hover": [
                                        {
                                            "text": "08. Floride Chemicals Factory Lorem ipsum dolor sit amet, consectetur smo adipiscing elit, sed do eiusmod tempor inciut labore et dolore magna ali.",
                                            "text2": "read more",
                                            "url": "https://preview.colorlib.com/theme/inds/work.html"
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                }
            ]
        }

class Blog(Resource):
    def get(seft):
        return {
            "data": [
                {
                    "banner": [
                        {
                            "image": "backgrond warna biru",
                            "text": "our blog"
                        }
                    ],
                    "content": [
                        {
                            "sidebar": [
                                {
                                    "group1": [
                                        {
                                            "placeholder": "Search Keyword",
                                            "defaultvalue": "null",
                                            "icon": "send",
                                            "url": "null",
                                            "button_click": [
                                                {
                                                    "text": "search",
                                                    "url": "null"
                                                }
                                            ]
                                        }
                                    ]
                                },
                                {
                                    "group2": [
                                        {
                                            "tittle_text": "category",
                                            "text1": "Resaurant food(37)",
                                            "text2": "Travel news(10)",
                                            "text3": "Modern technology(03)",
                                            "text4": "Product(11)",
                                            "text5": "Inspiration21",
                                            "text6": "Health Care (21)09"
                                        }
                                    ]
                                },
                                {
                                    "group3": [
                                        {
                                            "text": "Recent Post",
                                            "image": "laki laki",
                                            "text1": "From life was you fish...",
                                            "url": "https://preview.colorlib.com/theme/inds/single-blog.html",
                                            "text_date": "January 12, 2019"
                                        },
                                        {
                                            "image": "perempuan",
                                            "text1": "The Amazing Hubble",
                                            "url": "https://preview.colorlib.com/theme/inds/single-blog.html",
                                            "text_date": "02 Hours ago"
                                        },
                                        {
                                            "image": "astronomy",
                                            "text1": "Astronomy Or Astrology",
                                            "url": "https://preview.colorlib.com/theme/inds/single-blog.html",
                                            "text_date": "03 Hours ago"
                                        },
                                        {
                                            "image": "ruangan",
                                            "text1": "Asteroids telescope",
                                            "url": "https://preview.colorlib.com/theme/inds/single-blog.html",
                                            "text_date": "01 Hours ago"
                                        }
                                    ]
                                },
                                {
                                    "group4": [
                                        {
                                            "text": "Tag Clouds",
                                            "button_click": [
                                                {
                                                    "text1": "project",
                                                    "text2": "love",
                                                    "text3": "technology",
                                                    "text4": "travel",
                                                    "text5": "restaurant",
                                                    "text6": "life style",
                                                    "text7": "design",
                                                    "text8": "illustration"
                                                }
                                            ]
                                        }
                                    ]
                                },
                                {
                                    "group5": [
                                        {
                                            "text": "Instagram Feeds",
                                            "image1": "abstrack",
                                            "image2": "laki laki",
                                            "image3": "daun",
                                            "image4": "make up",
                                            "image5": "pantai",
                                            "image6": "minuman"
                                        }
                                    ]
                                },
                                {
                                    "group6": [
                                        {
                                            "text": "new-stellar",
                                            "placeholder": "Enter email",
                                            "defailtvalue": "null",
                                            "button_click": [
                                                {
                                                    "text": "subcribe",
                                                    "url": "null"
                                                }
                                            ]
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            "maincontent": [
                                {
                                    "group1": [
                                        {
                                            "image": "party",
                                            "textdate": "15 Jan",
                                            "tetxttitle": "Google inks pact for new 35-storey office",
                                            "url": "https://preview.colorlib.com/theme/inds/single-blog.html",
                                            "textdescription": "That dominion stars lights dominion divide years for fourth have don't stars is that he earth it first without heaven in place seed it second morning saying",
                                            "icon1": "profile",
                                            "text1":  "Travel, Lifestyle",
                                            "icon2": "chat",
                                            "tex2": " 03 Comments"
                                        }
                                    ]
                                },
                                {
                                    "group2": [
                                        {
                                            "image": "main hp",
                                            "textdate": "15 Jan",
                                            "tetxttitle": "Google inks pact for new 35-storey office",
                                            "url": "https://preview.colorlib.com/theme/inds/single-blog.html",
                                            "textdescription": "That dominion stars lights dominion divide years for fourth have don't stars is that he earth it first without heaven in place seed it second morning saying",
                                            "icon1": "profile",
                                            "text1":  "Travel, Lifestyle",
                                            "icon2": "chat",
                                            "tex2": " 03 Comments"
                                        }
                                    ]
                                },
                                {
                                    "group3": [
                                        {
                                            "image": "wanita bersepatu",
                                            "textdate": "15 Jan",
                                            "tetxttitle": "Google inks pact for new 35-storey office",
                                            "url": "https://preview.colorlib.com/theme/inds/single-blog.html",
                                            "textdescription": "That dominion stars lights dominion divide years for fourth have don't stars is that he earth it first without heaven in place seed it second morning saying",
                                            "icon1": "profile",
                                            "text1":  "Travel, Lifestyle",
                                            "icon2": "chat",
                                            "tex2": " 03 Comments"
                                        }
                                    ]
                                },
                                {
                                    "group4": [
                                        {
                                            "image": "mockup",
                                            "textdate": "15 Jan",
                                            "tetxttitle": "Google inks pact for new 35-storey office",
                                            "url": "https://preview.colorlib.com/theme/inds/single-blog.html",
                                            "textdescription": "That dominion stars lights dominion divide years for fourth have don't stars is that he earth it first without heaven in place seed it second morning saying",
                                            "icon1": "profile",
                                            "text1":  "Travel, Lifestyle",
                                            "icon2": "chat",
                                            "tex2": " 03 Comments"
                                        }
                                    ]
                                },
                                {
                                    "group5": [
                                        {
                                            "image": "cake",
                                            "textdate": "15 Jan",
                                            "tetxttitle": "Google inks pact for new 35-storey office",
                                            "url": "https://preview.colorlib.com/theme/inds/single-blog.html",
                                            "textdescription": "That dominion stars lights dominion divide years for fourth have don't stars is that he earth it first without heaven in place seed it second morning saying",
                                            "icon1": "profile",
                                            "text1":  "Travel, Lifestyle",
                                            "icon2": "chat",
                                            "tex2": " 03 Comments"
                                        }
                                    ]
                                }
                            ]
                        }
                    ],
                    "courosel": [
                        {
                            "icon1": "arrow_left",
                            "text_number": "1",
                            "icon2": "arrow_right",
                            "twxt_nmber": "2"
                        }
                    ]
                }
            ]
        }

class Single_Blog(Resource):
    def get(seft):
        return {
            "data": [
                {
                    "banner": [
                        {
                            "image": "backgrond warna biru",
                            "text": "our blog"
                        }
                    ],
                    "content": [
                        {
                            "sidebar": [
                                {
                                    "group1": [
                                        {
                                            "placeholder": "Search Keyword",
                                            "defaultvalue": "null",
                                            "icon": "send",
                                            "url": "null",
                                            "button_click": [
                                                {
                                                    "text": "search",
                                                    "url": "null"
                                                }
                                            ]
                                        }
                                    ]
                                },
                                {
                                    "group2": [
                                        {
                                            "tittle_text": "category",
                                            "text1": "Resaurant food(37)",
                                            "text2": "Travel news(10)",
                                            "text3": "Modern technology(03)",
                                            "text4": "Product(11)",
                                            "text5": "Inspiration21",
                                            "text6": "Health Care (21)09"
                                        }
                                    ]
                                },
                                {
                                    "group3": [
                                        {
                                            "text": "Recent Post",
                                            "image": "laki laki",
                                            "text1": "From life was you fish...",
                                            "url": "https://preview.colorlib.com/theme/inds/single-blog.html",
                                            "text_date": "January 12, 2019"
                                        },
                                        {
                                            "image": "perempuan",
                                            "text1": "The Amazing Hubble",
                                            "url": "https://preview.colorlib.com/theme/inds/single-blog.html",
                                            "text_date": "02 Hours ago"
                                        },
                                        {
                                            "image": "astronomy",
                                            "text1": "Astronomy Or Astrology",
                                            "url": "https://preview.colorlib.com/theme/inds/single-blog.html",
                                            "text_date": "03 Hours ago"
                                        },
                                        {
                                            "image": "ruangan",
                                            "text1": "Asteroids telescope",
                                            "url": "https://preview.colorlib.com/theme/inds/single-blog.html",
                                            "text_date": "01 Hours ago"
                                        }
                                    ]
                                },
                                {
                                    "group4": [
                                        {
                                            "text": "Tag Clouds",
                                            "button_click": [
                                                {
                                                    "text1": "project",
                                                    "text2": "love",
                                                    "text3": "technology",
                                                    "text4": "travel",
                                                    "text5": "restaurant",
                                                    "text6": "life style",
                                                    "text7": "design",
                                                    "text8": "illustration"
                                                }
                                            ]
                                        }
                                    ]
                                },
                                {
                                    "group5": [
                                        {
                                            "text": "Instagram Feeds",
                                            "image1": "abstrack",
                                            "image2": "laki laki",
                                            "image3": "daun",
                                            "image4": "make up",
                                            "image5": "pantai",
                                            "image6": "minuman"
                                        }
                                    ]
                                },
                                {
                                    "group6": [
                                        {
                                            "text": "new-stellar",
                                            "placeholder": "Enter email",
                                            "defailtvalue": "null",
                                            "button_click": [
                                                {
                                                    "text": "subcribe",
                                                    "url": "null"
                                                }
                                            ]
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            "maincontent": [
                                {
                                    "group1": [
                                        {
                                            "image": "party",
                                            "textdate": "15 Jan",
                                            "tetxttitle": "Google inks pact for new 35-storey office",
                                            "url": "https://preview.colorlib.com/theme/inds/single-blog.html",
                                            "textdescription": "MCSE boot camps have its supporters and its detractors. Some people do not understand why you should have to spend money on boot camp when you can get the MCSE study materials yourself at a fraction of the camp price. However, who has the willpower MCSE boot camps have its supporters and its detractors. Some people do not understand why you should have to spend money on boot camp when you can get the MCSE study materials yourself at a fraction of the camp price. However, who has the willpower to actually sit through a self-imposed MCSE training. who has the willpower to actually",
                                            "textdescription2": "MCSE boot camps have its supporters and its detractors. Some people do not understand why you should have to spend money on boot camp when you can get the MCSE study materials yourself at a fraction of the camp price. However, who has the willpower MCSE boot camps have its supporters and its detractors. Some people do not understand why you should have to spend money on boot camp when you can get the MCSE study materials yourself at a fraction of the camp price. However, who has the willpower to actually sit through a self-imposed MCSE training. who has the willpower to actually",
                                            "quote": "MCSE boot camps have its supporters and its detractors. Some people do not understand why you should have to spend money on boot camp when you can get the MCSE study materials yourself at a fraction of the camp price. However, who has the willpower to actually sit through a self-imposed MCSE training.",
                                            "icon1": "profile",
                                            "text1":  "Travel, Lifestyle",
                                            "icon2": "chat",
                                            "tex2": " 03 Comments"
                                        }
                                    ]
                                },
                                {
                                    "group2": [
                                        {
                                            "comment1": [
                                                {
                                                    "icon": "love",
                                                    "text": " Lily and 4 people like this",
                                                    "left": [
                                                        {
                                                            "image": "abstrack",
                                                            "hover": [
                                                                {
                                                                    "icon": "arrow",
                                                                    "url": "null"
                                                                }
                                                            ],
                                                            "text1": "Prev Post",
                                                            "text2": "Space The Final Frontier"
                                                        }
                                                    ],
                                                    "right": [
                                                        {
                                                            "image": "mockup",
                                                            "hover": [
                                                                {
                                                                    "icon": "arrow",
                                                                    "url": "null"
                                                                }
                                                            ],
                                                            "text1": "next Post",
                                                            "text2": "Telescopes 101"
                                                        }
                                                    ]
                                                },
                                                {
                                                    "image": "people profil",
                                                    "textname": "Harvard milan",
                                                    "comment": "Second divided from form fish beast made. Every of seas all gathered use saying you're, he our dominion twon Second divided from"
                                                }
                                            ]
                                        },
                                        {
                                            "comment2": [
                                                {
                                                    "text": "05 Comments"
                                                },
                                                {
                                                    "image": "people profil",
                                                    "textcoment": "Multiply sea night grass fourth day sea lesser rule open subdue female fill which them Blessed, give fill lesser bearing multiply sea night grass fourth day sea lesse",
                                                    "textname": "Emilly Blunt",
                                                    "textdate": "December 4, 2017 at 3:12 pm",
                                                    "click": [
                                                        {
                                                            "text": "reply",
                                                            "url": "null"
                                                        }
                                                    ]
                                                },
                                                {
                                                    "image": "people profil",
                                                    "textcoment": "Multiply sea night grass fourth day sea lesser rule open subdue female fill which them Blessed, give fill lesser bearing multiply sea night grass fourth day sea lesse",
                                                    "textname": "Emilly Blunt",
                                                    "textdate": "December 4, 2017 at 3:12 pm",
                                                    "click": [
                                                        {
                                                            "text": "reply",
                                                            "url": "null"
                                                        }
                                                    ]
                                                },
                                                {
                                                    "image": "people profil",
                                                    "textcoment": "Multiply sea night grass fourth day sea lesser rule open subdue female fill which them Blessed, give fill lesser bearing multiply sea night grass fourth day sea lesse",
                                                    "textname": "Emilly Blunt",
                                                    "textdate": "December 4, 2017 at 3:12 pm",
                                                    "click": [
                                                        {
                                                            "text": "reply",
                                                            "url": "null"
                                                        }
                                                    ]
                                                }
                                            ]
                                        },
                                        {
                                            "comment3": [
                                                {
                                                    "text": "leave a reply"
                                                },
                                                {
                                                    "box": [
                                                        {
                                                            "placeholder1": {
                                                                "text": "write comment"
                                                            }
                                                        },
                                                        {
                                                            "placeholder2": {
                                                                "text": "name"
                                                            }
                                                        },
                                                        {
                                                            "placeholder3": {
                                                                "text": "email"
                                                            }
                                                        },
                                                        {
                                                            "placeholder4": {
                                                                "text": "website"
                                                            }
                                                        }
                                                    ]
                                                },
                                                {
                                                    "button_click": [
                                                        {
                                                            "text": "send a message",
                                                            "url": "null"
                                                        }
                                                    ]
                                                }
                                            ]
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                }
            ]
        }

api.add_resource(Home, '/v1/home/')
api.add_resource(About_Us, '/v1/about_us/')
api.add_resource(Service, '/v1/service/')
api.add_resource(Works, '/v1/works/')
api.add_resource(Blog, '/v1/blog/')
api.add_resource(Single_Blog, '/v1/single_blog/')

@app.errorhandler(404)
def page_not_found(e):
    return {"error":"not found end point"}, 404

if __name__ == '__main__':
    app.run(debug=True)