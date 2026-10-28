# EINSTEIN Matchmaker: synthetic dataset

Data for the EINSTEIN track of the NTP Novi Sad Hackathon (30–31 October 2026): researchers at the University of Novi Sad and companies around NTP Novi Sad, for a system of agents that finds researcher–company pairs worth a joint project or an industrial PhD.

**Everything here is invented.** The people, companies, publications, projects and patents don't exist; any resemblance to real ones is a coincidence. The faculties are real and only set the scene. Real public data (ORCID, OpenAlex, CORDIS, Google Patents, Lens) is allowed too.

## Files

| File | What's in it |
| --- | --- |
| `data/researchers.json` | 37 researchers: title, faculty, department, fields, keywords, publications, projects, patents, what they're open to (`open_to`), industry experience, notes |
| `data/companies.json` | 20 companies: sector, size, what they do, products, tech, **challenges** (each with an id), plans, R&D capacity, past collaborations |
| `data/*.csv` | The same, flattened for a spreadsheet (UTF-8) |
| `docs/apis.md` | Open APIs for real data (OpenAlex, ORCID, CORDIS, EU calls, patents), with examples |
| `docs/example-industrial-phd-topic.md` | What a good industrial PhD proposal looks like |

Every publication, project and patent has an id (`SYN-PUB-0001`, `SYN-PRJ-001`, `SYN-PAT-001`), and every challenge too (`C05-CH1`). Cite them in your proposals and traces, so a reviewer can check each claim.

## Like real data

The records aren't clean. Some are incomplete, a few are written in Serbian (in Latin or Cyrillic script), and one person can turn up in two sources. Words can mean different things in different fields. Not every company has a good match. When yours doesn't, the right answer says so.

## Rules

- The system proposes collaborations. It doesn't score or rank people by their worth.
- A claim about a person (a publication, a skill, a patent) must come from the data or a public source you cite.
