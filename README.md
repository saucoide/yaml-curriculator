# yaml curriculator

A crappy script to generate a static html resume/cv from a yaml file in a bunch
of different themes

## Example

`uv run generate.py resume.yaml --themes fern-creek deser-sand`
`uv run generate.py resume.yaml --themes all --open`

Results are saved in the `output/` directory

yaml format, there is a an example resume.yaml filled in the repo


```yaml
basics:
  name: John Doe
  label: Full Stack Developer
  image: ../images/pic.png
  email: john.doe@example.com
  phone: "+1 111 1111 111"
  url: https://github.com/johndoe
  summary: >
    Passionate developer with 5+ years of experience in building scalable web
    applications. I love solving complex problems and learning new technologies.
  location:
    city: San Francisco
    country_code: US
    region: California
  profiles:
    - network: GitHub
      username: johndoe
      display_as: github.com/johndoe
      url: https://www.github.com/johndoe
    - network: LinkedIn
      username: johndoe
      display_as: linkedin.com/in/johndoe
      url: https://www.linkedin.com/in/johndoe

work:
  - company: Tech Solutions Inc.
    position: Senior Developer
    start_date: Jan 2020
    end_date: Present
    summary: >
      Leading a team of 5 developers to build a cloud-native SaaS platform.
      Improved system performance by 30% through code optimization and refactoring.
    highlights:
      - Python, Django, React, AWS, Docker

  - company: Creative Web Agency
   # ...

education:
  - institution: University of Technology
    area: Computer Science
    study_type: Bachelor
    start_date: Sep 2013
    end_date: May 2017
    summary: >
      Graduated with Honors. Capstone project focused on machine learning algorithms
      for image recognition.

skills:
  - name: Programming Languages
    keywords:
      - Python
      - JavaScript
      - TypeScript
      - Go
  - name: Frameworks & Tools
    keywords:
      - React
      - Django
      - Docker
      - Kubernetes
      - Git

languages:
  - English (Native)
  - Spanish (Intermediate)

certificates:
  - name: AWS Certified Solutions Architect
    date: "2021-08-15"
    issuer: Amazon Web Services
    url: "https://aws.amazon.com/verification"
```
