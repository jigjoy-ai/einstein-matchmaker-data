"""Builds the EINSTEIN track's synthetic dataset: fictional researchers and companies in Novi Sad.

Everything here is invented: people, companies, publications, projects and patents. Institutions are
real faculties of the University of Novi Sad, so the setting feels familiar; nobody in the data exists.

    python3 build.py   →  data/ (for participants), and jury/answer-key.json when jury/key.py is there
"""

import csv
import json
from pathlib import Path

ROOT = Path(__file__).parent
FTN = "Faculty of Technical Sciences"
TF = "Faculty of Technology"
POLJ = "Faculty of Agriculture"
PMF = "Faculty of Sciences"
MF = "Faculty of Medicine"
EF = "Faculty of Economics in Subotica"
FF = "Faculty of Philosophy"
GF = "Faculty of Civil Engineering Subotica"
BIO = "BioSense Institute"

pub_n = 0
prj_n = 0
pat_n = 0


def pubs(*items):
    """(title, year, venue, kind) → publications with synthetic ids."""
    global pub_n
    out = []
    for title, year, venue, kind in items:
        pub_n += 1
        out.append({"id": f"SYN-PUB-{pub_n:04d}", "title": title, "year": year, "venue": venue, "type": kind})
    return out


def projects(*items):
    """(title, program, role, years) → projects with synthetic ids."""
    global prj_n
    out = []
    for title, program, role, years in items:
        prj_n += 1
        out.append({"id": f"SYN-PRJ-{prj_n:03d}", "title": title, "program": program, "role": role, "years": years})
    return out


def patents(*items):
    """(title, year, status) → patents with synthetic ids."""
    global pat_n
    out = []
    for title, year, status in items:
        pat_n += 1
        out.append({"id": f"SYN-PAT-{pat_n:03d}", "title": title, "year": year, "status": status})
    return out


def researcher(id, name, title, faculty, department, fields, keywords, publications=(), project_list=(), patent_list=(),
               open_to=("industrial PhD supervision", "joint projects"), industry="", notes="", language="en"):
    return {
        "id": id,
        "name": name,
        "title": title,
        "institution": "University of Novi Sad" if faculty != BIO else "University of Novi Sad (BioSense Institute)",
        "faculty": faculty,
        "department": department,
        "fields": list(fields),
        "keywords": list(keywords),
        "publications": list(publications),
        "projects": list(project_list),
        "patents": list(patent_list),
        "open_to": list(open_to),
        "industry_experience": industry,
        "notes": notes,
        "language": language,
    }


R = [
    # ── Agriculture, remote sensing, agri-IoT ───────────────────────────────────────────────
    researcher(
        "R01", "Milica Stanković", "Research Professor", BIO, "Remote Sensing and GIS Group",
        ["remote sensing", "precision agriculture", "machine learning"],
        ["Sentinel-2", "crop yield prediction", "hyperspectral imaging", "time series", "soil moisture"],
        pubs(
            ("Early-season maize yield prediction from Sentinel-2 time series at parcel level", 2024, "Journal of Applied Earth Observation in Agriculture", "journal"),
            ("Hyperspectral indices for nitrogen stress in winter wheat under variable irrigation", 2023, "Precision Farming Letters", "journal"),
            ("Fusing radar and optical imagery for soil moisture mapping in the Pannonian plain", 2022, "International Symposium on Agricultural Remote Sensing", "conference"),
            ("Transfer learning for crop type maps when labels are scarce", 2021, "Remote Sensing Methods", "journal"),
        ),
        projects(
            ("AGROSAT: satellite monitoring of field crops in Vojvodina", "Science Fund of the Republic of Serbia (synthetic)", "principal investigator", "2022–2025"),
            ("SOILSCAN: soil health indicators from space", "Horizon Europe (synthetic)", "work package lead", "2023–2026"),
        ),
        industry="Advised two agri-tech startups on satellite data pipelines.",
    ),
    researcher(
        "R02", "Nenad Ilić", "Associate Professor", POLJ, "Department of Field and Vegetable Crops",
        ["agronomy", "irrigation", "decision support systems"],
        ["drip irrigation", "evapotranspiration", "irrigation scheduling", "soil moisture sensors", "sugar beet"],
        pubs(
            ("Evapotranspiration-based irrigation scheduling for sugar beet on chernozem", 2023, "Agricultural Water Use", "journal"),
            ("Low-cost capacitive soil moisture probes: calibration across soil types", 2021, "Sensors in Agronomy", "journal"),
            ("Deficit irrigation of vegetables in a changing climate", 2020, "Conference on Sustainable Field Crops", "conference"),
        ),
        projects(("WATERWISE: irrigation advice for smallholders", "Provincial Secretariat for Higher Education (synthetic)", "principal investigator", "2021–2023")),
        patents(("Capacitive soil moisture probe with a multi-depth sensing array", 2021, "granted")),
    ),
    researcher(
        "R03", "Ana Kovačević", "Assistant Professor", FTN, "Department of Power, Electronics and Telecommunications",
        ["wireless sensor networks", "embedded systems", "low-power electronics"],
        ["LoRaWAN", "energy harvesting", "battery life", "sensor nodes", "agricultural IoT"],
        pubs(
            ("Extending LoRaWAN node lifetime in sub-zero temperatures with adaptive duty cycling", 2024, "Journal of Low-Power Systems", "journal"),
            ("Solar energy harvesting for orchard sensor nodes: a two-year field study", 2023, "International Conference on IoT in Agriculture", "conference"),
            ("Packet loss in dense rural LoRa deployments", 2022, "Wireless Networks Review", "journal"),
        ),
        projects(("FIELDNET: rural sensor networks", "Science Fund of the Republic of Serbia (synthetic)", "researcher", "2022–2024")),
        industry="Spent two years designing sensor hardware at a telecom company before the PhD.",
    ),
    researcher(
        "R04", "Dragan Pavlović", "Full Professor", POLJ, "Department of Plant and Environmental Protection",
        ["entomology", "integrated pest management"],
        ["pheromone traps", "codling moth", "pest monitoring", "orchards", "image-based insect counting"],
        pubs(
            ("Codling moth flight dynamics in apple orchards of northern Serbia", 2022, "Journal of Applied Entomology Studies", "journal"),
            ("Counting moths in pheromone trap photos: agreement between experts and a neural network", 2024, "Plant Protection Science", "journal"),
            ("Forecasting spraying windows from trap counts and degree-days", 2020, "Symposium on Integrated Pest Management", "conference"),
        ),
        projects(("ORCHARD-IPM: pest warning service", "Ministry of Agriculture (synthetic)", "principal investigator", "2019–2023")),
    ),
    # ── Food technology and packaging ─────────────────────────────────────────────────────────
    researcher(
        "R05", "Jelena Marković", "Full Professor", TF, "Department of Food Preservation Engineering",
        ["food engineering", "packaging", "predictive microbiology"],
        ["shelf life", "modified atmosphere packaging", "berries", "cold chain", "predictive models"],
        pubs(
            ("Modified atmosphere packaging extends raspberry shelf life for export", 2023, "Journal of Food Process Engineering Studies", "journal"),
            ("Predictive growth models for Botrytis on soft fruit in the cold chain", 2022, "Food Microbiology Modelling", "journal"),
            ("Temperature abuse during transport: a sensor study of fruit exports", 2021, "International Food Congress", "conference"),
        ),
        projects(("FRESHROUTE: cold chain for Serbian berries", "Innovation Fund (synthetic)", "academic partner", "2022–2024")),
        industry="Worked with three fruit exporters on packaging trials.",
    ),
    researcher(
        "R06", "Stefan Đorđević", "Associate Professor", TF, "Department of Materials Engineering",
        ["polymer science", "biodegradable materials"],
        ["PLA", "starch films", "compostable packaging", "edible coatings", "barrier properties"],
        pubs(
            ("Starch–PLA blends with improved water vapour barrier", 2024, "Biopolymer Materials", "journal"),
            ("Antimicrobial edible coatings from plant extracts for fresh-cut fruit", 2022, "Food Packaging and Shelf Life Research", "journal"),
            ("Home compostability of bio-based films under Serbian conditions", 2021, "Conference on Green Materials", "conference"),
        ),
        patent_list=patents(("Starch-based compostable film with an antimicrobial plant extract", 2023, "pending")),
    ),
    researcher(
        "R07", "Ivana Lukić", "Research Associate", TF, "Department of Biotechnology",
        ["food waste valorization", "bioprocess engineering"],
        ["wheat bran", "fermentation", "dietary fibre", "bioactive compounds", "by-products"],
        pubs(
            ("Solid-state fermentation of wheat bran into a protein-rich ingredient", 2023, "Bioresource Valorization", "journal"),
            ("Extracting ferulic acid from milling by-products", 2021, "Journal of Cereal By-products", "journal"),
        ),
        projects(("BRANVALUE: from milling waste to food ingredients", "Science Fund of the Republic of Serbia (synthetic)", "principal investigator", "2023–2025")),
    ),
    # ── Power systems ─────────────────────────────────────────────────────────────────────────
    researcher(
        "R08", "Marko Petrović", "Full Professor", FTN, "Department of Power, Electronics and Telecommunications",
        ["power systems", "asset management", "high-voltage equipment"],
        ["power transformers", "dissolved gas analysis", "condition monitoring", "failure prediction", "distribution grid"],
        pubs(
            ("Predicting distribution transformer failures from dissolved gas analysis and load history", 2024, "Journal of Power Equipment Diagnostics", "journal"),
            ("Health indices for ageing transformer fleets", 2022, "International Conference on Grid Assets", "conference"),
            ("Thermal models of oil-immersed transformers under PV-driven reverse flow", 2021, "Power Delivery Research", "journal"),
        ),
        projects(("GRIDHEALTH: condition-based maintenance for the distribution grid", "Horizon Europe (synthetic)", "principal investigator", "2022–2025")),
        industry="Twelve years of joint work with distribution system operators.",
    ),
    researcher(
        "R09", "Milan Petrović", "Assistant Professor", FTN, "Department of Computing and Control Engineering",
        ["natural language processing", "machine learning"],
        ["transformer models", "Serbian language", "retrieval", "embeddings", "question answering"],
        pubs(
            ("A transformer model pre-trained on Serbian web text", 2024, "Workshop on Slavic Language Technology", "conference"),
            ("Dense retrieval for Serbian customer-support questions", 2023, "Journal of Language Engineering", "journal"),
            ("Handling Latin and Cyrillic script in one embedding space", 2022, "Conference on Computational Linguistics in the Balkans", "conference"),
        ),
        projects(("SRB-NLP: open language resources for Serbian", "Science Fund of the Republic of Serbia (synthetic)", "researcher", "2023–2026")),
    ),
    researcher(
        "R10", "Tamara Simić", "Associate Professor", FTN, "Department of Power, Electronics and Telecommunications",
        ["smart grids", "renewable integration", "forecasting"],
        ["PV forecasting", "demand response", "distribution system operators", "short-term load forecasting", "flexibility"],
        pubs(
            ("Day-ahead PV forecasting for distribution feeders with satellite cloud data", 2024, "Renewable Grid Integration", "journal"),
            ("Demand response potential of industrial consumers in Vojvodina", 2022, "European Energy Markets Conference", "conference"),
            ("Probabilistic short-term load forecasting with gradient boosting", 2021, "Journal of Energy Forecasting", "journal"),
        ),
        projects(("FLEXGRID-RS: flexibility markets for Serbia", "Horizon Europe (synthetic)", "researcher", "2023–2026")),
    ),
    researcher(
        "R11", "Bojan Radić", "Assistant Professor", FTN, "Department of Power, Electronics and Telecommunications",
        ["energy storage", "power electronics"],
        ["lithium-ion batteries", "state of health", "battery management systems", "second-life batteries", "Kalman filter"],
        pubs(
            ("State-of-health estimation of second-life EV batteries from partial charging curves", 2024, "Journal of Energy Storage Systems", "journal"),
            ("Cell balancing for repurposed battery packs", 2023, "Power Electronics Conference", "conference"),
        ),
    ),
    # ── Computing: vision, optimization, language, speech ─────────────────────────────────────
    researcher(
        "R12", "Nikola Stojanović", "Associate Professor", FTN, "Department of Computing and Control Engineering",
        ["computer vision", "machine learning", "edge computing"],
        ["defect detection", "industrial inspection", "few-shot learning", "edge inference", "anomaly detection"],
        pubs(
            ("Few-shot surface defect detection on reflective metal parts", 2024, "Journal of Industrial Vision", "journal"),
            ("Quantized detectors for real-time inspection on edge devices", 2023, "Embedded AI Conference", "conference"),
            ("Synthetic defect generation for visual quality control", 2022, "Machine Vision Applications Review", "journal"),
        ),
        projects(("VISIONQC: AI quality control for SMEs", "Innovation Fund (synthetic)", "academic partner", "2023–2025")),
        industry="Co-founded a computer vision consultancy (2016–2019).",
    ),
    researcher(
        "R13", "Sara Babić", "Teaching Assistant", FTN, "Department of Computing and Control Engineering",
        ["medical imaging"],
        ["image segmentation", "MRI", "U-Net"],
        pubs(("Brain tumour segmentation with limited annotations", 2024, "Student Conference on Biomedical Computing", "conference")),
        open_to=["joint projects"],
        notes="PhD candidate, expected to defend in 2026.",
    ),
    researcher(
        "R14", "Luka Vuković", "Full Professor", PMF, "Department of Mathematics and Informatics",
        ["operations research", "combinatorial optimization"],
        ["vehicle routing", "time windows", "metaheuristics", "last-mile delivery", "scheduling"],
        pubs(
            ("An adaptive large neighbourhood search for routing with time windows and split deliveries", 2023, "Journal of Optimization in Logistics", "journal"),
            ("Same-day delivery with dynamic orders: a rolling-horizon approach", 2022, "Transportation Science Letters", "journal"),
            ("Scheduling with machine availability constraints", 2020, "Conference on Combinatorial Optimization", "conference"),
        ),
        projects(("LASTMILE-NS: city logistics for Novi Sad", "Provincial Secretariat for Higher Education (synthetic)", "principal investigator", "2021–2023")),
    ),
    researcher(
        "R15", "Katarina Nikolić", "Associate Professor", FF, "Department of Serbian Language and Linguistics",
        ["corpus linguistics", "morphology"],
        ["Serbian morphology", "lemmatization", "corpora", "inflection", "spelling variants"],
        pubs(
            ("A lemmatizer for Serbian that handles both scripts", 2023, "Journal of Slavic Linguistics Tools", "journal"),
            ("Inflection and search: why Serbian queries miss relevant documents", 2022, "Conference on South Slavic Languages", "conference"),
        ),
        projects(("KORPUS-NS: a reference corpus of contemporary Serbian", "Ministry of Science (synthetic)", "principal investigator", "2020–2024")),
    ),
    researcher(
        "R16", "Dušan Milošević", "Research Associate", FTN, "Department of Computing and Control Engineering",
        ["speech technology"],
        ["automatic speech recognition", "speech synthesis", "Serbian", "call centres", "noise robustness"],
        pubs(
            ("Noise-robust Serbian speech recognition for telephone audio", 2024, "Speech Technology Journal", "journal"),
            ("A Serbian text-to-speech voice built from 20 hours of audio", 2022, "Interspeech-style Workshop on Low-Resource Speech", "conference"),
        ),
        industry="Built the speech pipeline of a call-centre product (2018–2021).",
    ),
    # ── Biomedical ────────────────────────────────────────────────────────────────────────────
    researcher(
        "R17", "Maja Popović", "Associate Professor", FTN, "Department of Biomedical Engineering",
        ["biomedical signal processing", "wearables"],
        ["ECG", "atrial fibrillation", "arrhythmia detection", "false alarms", "accelerometer"],
        pubs(
            ("Cutting false atrial fibrillation alarms in patch ECG with motion-aware filtering", 2024, "Journal of Biomedical Signal Analysis", "journal"),
            ("Single-lead ECG arrhythmia classification on a microcontroller", 2022, "Conference on Medical Devices Engineering", "conference"),
            ("Activity recognition from chest-worn accelerometers", 2021, "Wearable Sensing Review", "journal"),
        ),
        projects(("HEARTWATCH: remote cardiac monitoring", "Science Fund of the Republic of Serbia (synthetic)", "principal investigator", "2022–2025")),
    ),
    researcher(
        "R18", "Goran Tomić", "Full Professor", MF, "Department of Internal Medicine (Cardiology)",
        ["cardiology", "clinical research"],
        ["heart failure", "telemonitoring", "clinical trials", "atrial fibrillation", "ethics approval"],
        pubs(
            ("Telemonitoring after heart failure hospitalisation: a randomised study", 2023, "Cardiology Practice Journal", "journal"),
            ("Screening for silent atrial fibrillation in older adults", 2021, "Congress of Cardiology", "conference"),
        ),
        projects(("TELECARE-HF", "Ministry of Health (synthetic)", "principal investigator", "2021–2024")),
        notes="Leads clinical validation studies; needs device makers to cover study costs.",
    ),
    researcher(
        "R19", "Jovana Ristić", "Assistant Professor", BIO, "Sensors and Microsystems Group",
        ["biosensors", "printed electronics"],
        ["electrochemical sensors", "screen printing", "nitrate", "milk quality", "point-of-care"],
        pubs(
            ("Screen-printed electrodes for on-farm nitrate measurement", 2023, "Sensors and Microsystems", "journal"),
            ("Detecting somatic cells in milk with an impedance sensor", 2022, "Conference on Agri-Food Sensors", "conference"),
        ),
        patent_list=patents(("Screen-printed electrode for nitrate detection in water", 2022, "granted")),
    ),
    # ── Chemistry, water, buildings ───────────────────────────────────────────────────────────
    researcher(
        "R20", "Aleksandar Marić", "Full Professor", TF, "Department of Chemical Engineering",
        ["chemical engineering", "separation processes"],
        ["membrane filtration", "fouling", "wastewater treatment", "process intensification"],
        pubs(
            ("Ultrasound-assisted cleaning cuts membrane fouling in dairy wastewater", 2023, "Journal of Membrane Processes", "journal"),
            ("Modelling fouling in ceramic membranes", 2021, "Chemical Process Engineering", "journal"),
        ),
        industry="Consultant to food factories on wastewater lines.",
    ),
    researcher(
        "R21", "Teodora Filipović", "Research Associate", PMF, "Department of Chemistry, Biochemistry and Environmental Protection",
        ["environmental chemistry", "water treatment"],
        ["photocatalysis", "micropollutants", "pharmaceuticals", "advanced oxidation", "TiO2"],
        pubs(
            ("Photocatalytic removal of diclofenac and carbamazepine from hospital wastewater", 2024, "Water Chemistry Research", "journal"),
            ("Pharmaceutical residues in the Danube near Novi Sad: a sampling campaign", 2022, "Environmental Monitoring Letters", "journal"),
        ),
    ),
    researcher(
        "R22", "Zoran Kostić", "Associate Professor", GF, "Department of Hydraulic Engineering",
        ["hydraulics", "water distribution networks"],
        ["leak detection", "leak localization", "pressure management", "hydraulic models", "district metered areas"],
        pubs(
            ("Locating leaks from pressure sensors and a calibrated hydraulic model", 2023, "Journal of Water Network Engineering", "journal"),
            ("Pressure management cuts losses in a mid-size town", 2021, "Conference on Urban Water", "conference"),
        ),
        projects(("AQUALOSS: reducing water losses in Vojvodina towns", "Provincial Secretariat (synthetic)", "principal investigator", "2022–2024")),
    ),
    researcher(
        "R23", "Danica Savić", "Assistant Professor", FTN, "Department of Civil Engineering and Geodesy",
        ["building information modelling", "energy efficiency"],
        ["BIM", "digital twins", "energy retrofit", "public buildings", "thermal simulation"],
        pubs(
            ("Digital twins for planning the energy retrofit of school buildings", 2024, "Building Performance Journal", "journal"),
            ("From BIM to energy simulation without manual remodelling", 2022, "Conference on Digital Construction", "conference"),
        ),
    ),
    # ── Economics, logistics, finance ─────────────────────────────────────────────────────────
    researcher(
        "R24", "Ognjen Lazić", "Assistant Professor", EF, "Department of Business Informatics",
        ["supply chain analytics", "forecasting"],
        ["demand forecasting", "retail", "promotions", "inventory", "intermittent demand"],
        pubs(
            ("Forecasting intermittent demand in regional retail chains", 2023, "Journal of Retail Analytics", "journal"),
            ("Promotion effects on store-level demand", 2022, "Balkan Conference on Operations", "conference"),
        ),
    ),
    researcher(
        "R27", "Branislav Žarković", "Full Professor", EF, "Department of Finance and Banking",
        ["credit risk", "SME finance"],
        ["credit scoring", "thin-file borrowers", "explainable models", "alternative data", "regulation"],
        pubs(
            ("Scoring micro-enterprises with little credit history", 2023, "Journal of Banking and Finance Studies", "journal"),
            ("Explaining credit decisions to supervisors: a case study", 2022, "Conference on Financial Regulation", "conference"),
        ),
        industry="Former head of risk at a regional bank (2005–2012).",
    ),
    researcher(
        "R28", "Anja Todić", "Assistant Professor", EF, "Department of Marketing",
        ["behavioural economics", "consumer research"],
        ["pricing", "surveys", "willingness to pay", "experiments"],
        pubs(("Willingness to pay for locally produced food in Vojvodina", 2023, "Journal of Consumer Studies", "journal")),
    ),
    # ── Security, embedded, robotics, manufacturing ───────────────────────────────────────────
    researcher(
        "R25", "Vuk Đukić", "Associate Professor", FTN, "Department of Computing and Control Engineering",
        ["cybersecurity", "network security"],
        ["intrusion detection", "industrial control systems", "anomaly detection", "IoT security", "threat modelling"],
        pubs(
            ("Unsupervised anomaly detection on Modbus traffic", 2024, "Journal of Industrial Security", "journal"),
            ("Threat modelling for smart building controllers", 2022, "Conference on Applied Cybersecurity", "conference"),
        ),
        projects(("SECURE-ICS: security monitoring for factories", "Innovation Fund (synthetic)", "academic partner", "2023–2025")),
    ),
    researcher(
        "R26", "Mina Jakovljević", "Teaching Assistant", PMF, "Department of Mathematics and Informatics",
        ["cryptography"],
        ["post-quantum cryptography", "digital signatures"],
        open_to=["joint projects"],
        notes="Profile incomplete: no publications listed yet.",
    ),
    researcher(
        "R29", "Igor Matić", "Associate Professor", FTN, "Department of Computing and Control Engineering",
        ["embedded software", "automotive systems"],
        ["AUTOSAR", "ISO 26262", "functional safety", "hardware-in-the-loop", "model-based testing"],
        pubs(
            ("Generating ISO 26262 test cases from Simulink models", 2023, "Journal of Automotive Software", "journal"),
            ("A low-cost hardware-in-the-loop bench for body control modules", 2022, "Embedded Systems Conference", "conference"),
        ),
        industry="Eight years with an automotive software supplier in Novi Sad.",
    ),
    researcher(
        "R30", "Sofija Janković", "Assistant Professor", FTN, "Department of Mechatronics, Robotics and Automation",
        ["robotics"],
        ["collaborative robots", "motion planning", "ROS 2", "bin picking"],
        pubs(("Bin picking with a collaborative robot and a depth camera", 2024, "Robotics Applications Journal", "journal")),
    ),
    researcher(
        "R31", "Dejan Bogdanović", "Full Professor", FTN, "Department of Production Engineering",
        ["additive manufacturing", "design optimization"],
        ["metal 3D printing", "selective laser melting", "porosity", "topology optimization", "support structures"],
        pubs(
            ("Process windows that reduce porosity in SLM-printed 316L steel", 2023, "Journal of Additive Manufacturing Processes", "journal"),
            ("Topology optimization with self-supporting constraints", 2022, "Conference on Advanced Manufacturing", "conference"),
        ),
        patent_list=patents(("Lattice support structure that breaks away cleanly after printing", 2016, "expired")),
    ),
    researcher(
        "R32", "Marija Cvetković", "Associate Professor", FTN, "Department of Industrial Engineering and Management",
        ["industrial engineering", "production planning"],
        ["production scheduling", "OEE", "lean manufacturing", "job shop"],
        pubs(("Scheduling a job shop of 3D printers with build-plate nesting", 2024, "Journal of Production Planning", "journal")),
    ),
    # ── Environment, livestock ────────────────────────────────────────────────────────────────
    researcher(
        "R33", "Uroš Kecman", "Research Associate", PMF, "Department of Geography, Tourism and Hotel Management",
        ["climatology", "GIS"],
        ["drought indices", "climate data", "spatial analysis"],
        pubs(("Drought trends in Vojvodina, 1961–2023", 2024, "Climate Research Letters", "journal")),
    ),
    researcher(
        "R34", "Nevena Bošković", "Associate Professor", POLJ, "Department of Animal Science",
        ["animal science", "precision livestock farming"],
        ["dairy cattle", "mastitis", "activity collars", "rumination", "early disease detection"],
        pubs(
            ("Rumination drops from collar sensors predict clinical mastitis two days early", 2024, "Journal of Dairy Precision Farming", "journal"),
            ("Heat stress and milk yield on Vojvodina dairy farms", 2022, "Livestock Science Conference", "conference"),
        ),
        projects(("SMARTHERD: sensor-based herd health", "Science Fund of the Republic of Serbia (synthetic)", "principal investigator", "2023–2026")),
    ),
    # ── Deliberately imperfect records ────────────────────────────────────────────────────────
    researcher(
        "R35", "Filip Mitrović", "PhD student", FTN, "Department of Computing and Control Engineering",
        [], ["blockchain", "smart contracts"],
        open_to=[],
        notes="Only keywords are known.",
    ),
    researcher(
        "R36", "Јелена Марковић", "редовни професор", "Технолошки факултет", "Катедра за инжењерство конзервисане хране",
        ["прехрамбено инжењерство", "амбалажа"],
        ["рок трајања", "паковање у модификованој атмосфери", "малине"],
        [],  # filled in below with R05's own first publication, as the second source lists it
        open_to=[],
        notes="Imported from a second source (Cyrillic).",
        language="sr-Cyrl",
    ),
    researcher(
        "R37", "Radomir Ćosić", "Professor Emeritus", FTN, "Department of Power, Electronics and Telecommunications",
        ["power systems"],
        ["power transformers", "insulation", "high voltage"],
        pubs(("Insulation ageing in power transformers: forty years of field data", 2019, "Journal of High Voltage Practice", "journal")),
        open_to=["consulting"],
        notes="Retired; no longer supervises PhD students.",
    ),
]


def company(id, name, sector, employees, founded, about, products, tech, challenges, plans, rd="", history="", language="en", location="NTP Novi Sad"):
    return {
        "id": id,
        "name": name,
        "sector": sector,
        "employees": employees,
        "founded": founded,
        "location": location,
        "about": about,
        "products": products,
        "tech": tech,
        "challenges": [{"id": f"{id}-CH{i + 1}", "text": c} for i, c in enumerate(challenges)],
        "plans": plans,
        "rd_capacity": rd,
        "past_collaborations": history,
        "language": language,
    }


C = [
    company("C01", "AgroLens d.o.o.", "Agri-tech software", 24, 2019,
            "Farm management software for mid-size grain farms in Vojvodina and Hungary: field records, spraying plans, satellite crop maps.",
            ["AgroLens Field (web and mobile)", "crop health maps"], ["Python", "PostGIS", "Sentinel Hub", "React Native"],
            ["Farmers want a yield estimate per parcel by mid-June, but our maps only show crop vigour.",
             "Ground truth for soil moisture costs too much: probes are expensive and we can't place them on every parcel."],
            "Launch a yield-forecast product for 2027 and expand to Romania.", rd="Two data scientists.", history="None with the university yet."),
    company("C02", "Polje Senzor d.o.o.", "IoT hardware", 9, 2021,
            "Pravimo bežične senzorske stanice za voćnjake: temperatura, vlažnost lista, padavine. Stanice rade na bateriju i šalju podatke preko LoRaWAN mreže.",
            ["PS-Orchard stanica", "aplikacija za upozorenja na mraz"], ["C", "STM32", "LoRaWAN", "Node.js"],
            ["Baterije u stanicama zimi traju upola kraće nego leti, pa voćari moraju da ih menjaju usred sezone.",
             "Voćari ručno broje leptire na feromonskim klopkama; hteli bismo da kamera na klopci to radi sama."],
            "Nova generacija stanica sa kamerom 2027.", rd="Dva inženjera hardvera.", history="Diplomski radovi studenata FTN-a.", language="sr"),
    company("C03", "FreshPak Solutions", "Packaging", 60, 2012,
            "Packaging for fresh fruit and vegetables, mostly for exporters of berries to the EU.",
            ["punnets", "lidding films", "export cartons"], ["film extrusion", "thermoforming"],
            ["Raspberries for Germany arrive with mould on day 9; buyers want 14 days.",
             "Big retailers will stop taking conventional plastic lidding film by 2028; we need a compostable one that still seals."],
            "Compostable range by 2028.", rd="Quality lab with three technologists.", history="Tested packaging with a faculty lab in 2020."),
    company("C04", "Zlatni Klas Mlin a.d.", "Food processing (milling)", 140, 1974,
            "Flour mill near Novi Sad producing wheat flour and semolina.",
            ["wheat flour", "semolina", "animal feed bran"], ["SCADA", "SAP"],
            ["We sell 18,000 tonnes of bran a year as cheap animal feed; we'd like a higher-value use.",
             "Electricity is our second-largest cost and peaks at bad times."],
            "Diversify into food ingredients.", rd="No R&D department.", history="None.", location="Novi Sad"),
    company("C05", "GridSense Analytics", "Energy software", 31, 2017,
            "Analytics for electricity distribution operators in the Western Balkans: asset registers, outage analysis, network planning.",
            ["GridSense Assets", "outage dashboards"], ["Python", "TimescaleDB", "Azure"],
            ["Operators want to know which distribution transformers will fail next year; they have dissolved gas analysis results and load data, but no model.",
             "Rooftop PV is changing feeder loads; operators need a day-ahead forecast per feeder."],
            "A predictive maintenance module in 2027.", rd="Five engineers, one with a PhD.", history="Two master's theses supervised jointly."),
    company("C06", "VoltCell Storage", "Energy storage", 15, 2022,
            "Builds stationary battery storage from second-life electric vehicle batteries for farms and small factories.",
            ["VoltCell 50 kWh cabinet"], ["BMS firmware", "CAN", "Python"],
            ["We can't tell how healthy a used battery module is without a full test cycle that takes 20 hours."],
            "Scale to 5 MWh a year.", rd="Three engineers.", history="None."),
    company("C07", "LinguaBot d.o.o.", "Conversational AI", 22, 2020,
            "Customer-support chatbots for banks and telecoms in Serbia.",
            ["LinguaBot Assist", "knowledge-base search"], ["Python", "Elasticsearch", "LLM APIs"],
            ["Our search misses answers because Serbian words change form (e.g. 'kartica', 'karticu', 'karticom') and users mix Latin and Cyrillic.",
             "Clients want the bot on the phone too; speech recognition for Serbian is poor on call audio."],
            "Voice channel in 2027.", rd="Four ML engineers.", history="Internships for FTN students."),
    company("C08", "CardioTrack d.o.o.", "Medical devices", 12, 2021,
            "A 7-day ECG patch with an app for cardiologists.",
            ["CardioTrack patch", "clinician portal"], ["embedded C", "Python", "AWS"],
            ["Too many false atrial fibrillation alarms when patients move.",
             "We need a clinical validation study in Serbia before CE marking."],
            "CE mark in 2027.", rd="Two biomedical engineers.", history="None."),
    company("C09", "InspektAI", "Industrial software", 18, 2020,
            "Visual quality control for factories: cameras on the line, software that flags defects.",
            ["InspektAI Line", "defect dashboards"], ["PyTorch", "NVIDIA Jetson", "C++"],
            ["Scratches on polished metal parts: reflections fool our model, and clients only have a few dozen defect photos.",
             "Clients want inference on cheaper edge devices than Jetson."],
            "Enter the automotive supply chain.", rd="Six ML engineers.", history="Hackathon sponsor in 2024."),
    company("C10", "HidroLogik d.o.o.", "Water software", 11, 2018,
            "Software for municipal water utilities: network maps, meter data, billing integration.",
            ["HidroLogik Net"], ["QGIS", "PostgreSQL", "EPANET"],
            ["Utilities lose 30–40% of water; they have pressure sensors in a few zones but can't say where the leak is.",
             "Forecasting daily water demand for pumping plans."],
            "Leak module for 2027.", rd="Two engineers.", history="None."),
    company("C11", "ReVita Water", "Environmental engineering", 27, 2014,
            "Designs and builds wastewater treatment units for food and pharmaceutical plants.",
            ["ReVita MBR units", "service contracts"], ["membrane bioreactors", "PLC"],
            ["A pharmaceutical client must remove drug residues (diclofenac, carbamazepine) that our biological step doesn't catch.",
             "Membranes in dairy plants foul quickly and need cleaning every week."],
            "Pharma-grade line by 2028.", rd="Process engineer and a lab technician.", history="Sampling campaign with a faculty in 2019."),
    company("C12", "BuildTwin d.o.o.", "Construction consulting", 14, 2019,
            "BIM modelling and consulting for public building projects.",
            ["BIM models", "energy audits"], ["Revit", "IFC", "EnergyPlus"],
            ["Cities want to retrofit 40 schools but don't know which to do first for the biggest energy savings per dinar."],
            "Digital-twin service for municipalities.", rd="One energy engineer.", history="None."),
    company("C13", "RouteWise", "Logistics software", 35, 2016,
            "Route planning and delivery tracking for couriers and retail chains.",
            ["RouteWise Planner", "driver app"], ["Java", "OR-Tools", "Kafka"],
            ["Same-day deliveries with narrow time windows: our planner takes too long when orders change during the day.",
             "Retail clients ask us to forecast store demand so deliveries match it."],
            "Dynamic re-planning in 2027.", rd="Optimization team of three.", history="Student projects with PMF."),
    company("C14", "SecureEdge Labs", "Cybersecurity", 19, 2019,
            "Security monitoring for factories and building management systems.",
            ["EdgeWatch sensor", "SOC service"], ["Zeek", "Rust", "Python"],
            ["We need to detect unusual behaviour on Modbus and BACnet networks without labelled attack data.",
             "Clients ask whether our firmware signing will survive quantum computers."],
            "Certify under the EU Cyber Resilience Act.", rd="Four security engineers.", history="None."),
    company("C15", "Kredo Fintech", "Fintech", 26, 2020,
            "Online loans for micro and small businesses.",
            ["Kredo SME loans"], ["Python", "dbt", "Snowflake"],
            ["Micro firms often have under a year of history; our scoring rejects good borrowers.",
             "The central bank wants every automated decision explained."],
            "Expand to North Macedonia.", rd="Data team of five.", history="None."),
    company("C16", "DriveCore Software", "Automotive software", 85, 2010,
            "Embedded software services for automotive tier-1 suppliers.",
            ["body control software", "testing services"], ["AUTOSAR", "C", "Simulink", "dSPACE"],
            ["Writing ISO 26262 test cases by hand takes most of our verification budget.",
             "We need a cheaper hardware-in-the-loop bench for smaller projects."],
            "A test-automation product line.", rd="Twenty engineers in verification.", history="Guest lectures at FTN."),
    company("C17", "PrintMetal 3D", "Additive manufacturing", 13, 2018,
            "Metal 3D printing service for tooling and spare parts.",
            ["SLM printing", "post-processing"], ["SLM machines", "Materialise Magics"],
            ["Porosity in 316L parts fails customer pressure tests in about 1 of 12 builds.",
             "Four printers, many small orders: we schedule builds by hand."],
            "Aerospace certification.", rd="Two application engineers.", history="Thesis on support structures (2015)."),
    company("C18", "MlekoSmart d.o.o.", "Agri-tech", 8, 2022,
            "Ogrlice za krave koje mere aktivnost i preživanje i aplikacija za farmere.",
            ["MlekoSmart ogrlica"], ["nRF52", "Kotlin", "Python"],
            ["Farmeri žele upozorenje na mastitis pre nego što se vide simptomi."],
            "Izlazak na tržište Hrvatske.", rd="Jedan inženjer.", history="Nema.", language="sr"),
    company("C19", "NebulaQ", "Quantum software", 6, 2023,
            "Quantum algorithms for drug discovery clients abroad.",
            ["NebulaQ SDK"], ["Qiskit", "Python"],
            ["Error mitigation on today's noisy quantum hardware for molecular simulation."],
            "Partner with a quantum hardware vendor.", rd="Four physicists.", history="None."),
    company("C20", "HempTex Vojvodina", "Textiles", 40, 2017,
            "Grows and processes industrial hemp into fibre for textiles.",
            ["hemp yarn", "non-woven mats"], ["decortication line"],
            ["Our decortication line damages long fibres, which lowers the price we get."],
            "A spinning line in 2028.", rd="None.", history="None.", location="Bačka Palanka"),
]

# R36 is R05 seen in another source: the same publication, under the same id.
_r05 = next(r for r in R if r["id"] == "R05")
next(r for r in R if r["id"] == "R36")["publications"] = [_r05["publications"][0]]
R.sort(key=lambda r: int(r["id"][1:]))

# The jury's answer key (expected pairs and the traps) lives in jury/key.py, outside the repo.
try:
    from jury.key import key as jury_key
except ImportError:
    jury_key = None


def main():
    data = ROOT / "data"
    jury = ROOT / "jury"
    data.mkdir(exist_ok=True)
    ids = [r["id"] for r in R] + [c["id"] for c in C]
    assert len(ids) == len(set(ids)), "duplicate ids"
    challenges = [x["id"] for c in C for x in c["challenges"]]
    KEY = jury_key(R) if jury_key else None
    if KEY:
        for ch, rs in KEY["strong"].items():
            assert any(ch == x["id"] for c in C for x in c["challenges"]), ch
            assert all(r in {x["id"] for x in R} for r in rs), (ch, rs)
        assert set(challenges) == set(KEY["strong"]), set(challenges) ^ set(KEY["strong"])

    meta = {
        "name": "EINSTEIN Matchmaker synthetic dataset",
        "version": "1.0",
        "note": "Synthetic. Every person, company, publication, project and patent is invented; any resemblance to real ones is a coincidence. Institutions are real faculties of the University of Novi Sad, used as a setting only.",
    }
    (data / "researchers.json").write_text(json.dumps({**meta, "researchers": R}, ensure_ascii=False, indent=2) + "\n")
    (data / "companies.json").write_text(json.dumps({**meta, "companies": C}, ensure_ascii=False, indent=2) + "\n")

    with open(data / "researchers.csv", "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        w.writerow(["id", "name", "title", "faculty", "department", "fields", "keywords", "publications", "projects", "patents", "open_to", "industry_experience", "notes", "language"])
        for r in R:
            w.writerow([r["id"], r["name"], r["title"], r["faculty"], r["department"], "; ".join(r["fields"]), "; ".join(r["keywords"]),
                        " | ".join(f'{p["id"]}: {p["title"]} ({p["year"]}, {p["venue"]})' for p in r["publications"]),
                        " | ".join(f'{p["id"]}: {p["title"]} ({p["program"]}, {p["role"]}, {p["years"]})' for p in r["projects"]),
                        " | ".join(f'{p["id"]}: {p["title"]} ({p["year"]}, {p["status"]})' for p in r["patents"]),
                        "; ".join(r["open_to"]), r["industry_experience"], r["notes"], r["language"]])
    with open(data / "companies.csv", "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        w.writerow(["id", "name", "sector", "employees", "founded", "location", "about", "products", "tech", "challenges", "plans", "rd_capacity", "past_collaborations", "language"])
        for c in C:
            w.writerow([c["id"], c["name"], c["sector"], c["employees"], c["founded"], c["location"], c["about"], "; ".join(c["products"]), "; ".join(c["tech"]),
                        " | ".join(f'{x["id"]}: {x["text"]}' for x in c["challenges"]), c["plans"], c["rd_capacity"], c["past_collaborations"], c["language"]])

    if KEY:
        (jury / "answer-key.json").write_text(json.dumps(KEY, ensure_ascii=False, indent=2) + "\n")
    print(f"{len(R)} researchers, {len(C)} companies, {len(challenges)} challenges, {pub_n} publications, {prj_n} projects, {pat_n} patents")


if __name__ == "__main__":
    main()
