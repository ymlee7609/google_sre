---
title: "Results of Postmortem Analysis"
book: "The Site Reliability Workbook"
part: "Appendix C"
type: "appendix"
source_url: "https://sre.google/workbook/postmortem-analysis/"
---

# Results of Postmortem Analysis

At Google, we have a standard [postmortem template](../../sre-book/example-postmortem/) that allows us to consistently capture the incident root cause and trigger, which enables trend analysis. We use this trend analysis to help us target improvements that address systemic root-cause types, such as faulty software interface design or immature change deployment planning. [Table C-1](#top_eight_outage_triggerscomma_2010en_das) shows the breakdown of our top eight triggers for outages, based on a sample of thousands of postmortems over the last seven years.

|                         |     |
|-------------------------|-----|
| Binary push             | 37% |
| Configuration push      | 31% |
| User behavior change    | 9%  |
| Processing pipeline     | 6%  |
| Service provider change | 5%  |
| Performance decay       | 5%  |
| Capacity management     | 5%  |
| Hardware                | 2%  |

Table C-1. Top eight outage triggers, 2010–2017 {#top_eight_outage_triggerscomma_2010en_das}

[Table C-2](#top_five_root_cause_categories_for_outag) presents the top five contributing root-cause categories.

|                             |        |
|-----------------------------|--------|
| Software                    | 41.35% |
| Development process failure | 20.23% |
| Complex system behaviors    | 16.90% |
| Deployment planning         | 6.74%  |
| Network failure             | 2.75%  |

Table C-2. Top five root-cause categories for outages {#top_five_root_cause_categories_for_outag}
