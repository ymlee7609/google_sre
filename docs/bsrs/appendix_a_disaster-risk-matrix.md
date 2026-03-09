---
title: "A Disaster Risk Assessment Matrix"
book: "Building Secure and Reliable Systems"
part: "Appendix A"
type: "appendix"
source_url: "https://google.github.io/building-secure-and-reliable-systems/raw/appa.html"
---

# A Disaster Risk Assessment Matrix

For a thorough disaster risk analysis, we recommend ranking the risks facing your organization by using a standardized matrix that accounts for each risk’s probability of occurrence and its potential impact to the organization. [#sample_disaster_risk_assessment_matrix](#sample_disaster_risk_assessment_matrix) is a sample risk assessment matrix that both large and small organizations can tailor to the specifics of their systems.

To use the matrix, assess the values appropriate for each of the columns of probability and impact. As we emphasize in [Chapter 16](ch16.html#onesix_disaster_planning), these values are likely dependent on what your organization does, its infrastructure, and where it is located. An organization operating out of Los Angeles, CA, in the US may have a higher likelihood of experiencing an earthquake than an organization operating out of Hamburg, Germany. If your organization has offices in many locations, you may even want to do a risk assessment per location.

Once you’ve calculated the probability and impact values, multiply them to determine the rank of each risk. The resulting values can be used to order the risks from highest to lowest, which serves as a guide for prioritization and preparation. A risk that ranks 0.8 will likely require more immediate attention than risks that have a value of 0.5 or 0.3. Be sure to develop response plans for the most critical risks your organization faces.

<table id="sample_disaster_risk_assessment_matrix" class="custom_table" style="width:100%;">
<caption>Sample disaster risk assessment matrix</caption>
<colgroup>
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr class="header">
<th>Theme</th>
<th>Risk</th>
<th>Probability of occurrence within a year</th>
<th>Impact to organization if risk occurs</th>
<th>Ranking</th>
<th>Names of systems impacted by risk</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td> </td>
<td> </td>
<td><em>Almost never: 0.0 Unlikely: 0.2 Somewhat unlikely : 0.4</em><br />
<em>Likely: 0.6</em><br />
<em>Highly likely: 0.8</em><br />
<em>Inevitable :1.0</em></td>
<td><em>Negligible: 0.0</em><br />
<em>Minimal: 0.2</em><br />
<em>Moderate: 0.5</em><br />
<em>Severe : 0.8</em><br />
<em>Critical: 1.0</em></td>
<td><em>Probability x impact</em></td>
<td> </td>
</tr>
<tr class="even">
<td rowspan="4">Environmental</td>
<td>Earthquake</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Flood</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Fire</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Hurricane</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td rowspan="4">Infrastructure reliability</td>
<td>Power outage</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Loss of internet connectivity</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Authentication system down</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>High system latency/<br />
infrastructure slowdown</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td rowspan="9">Security</td>
<td>System compromise</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Insider theft of intellectual property</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>DDos/DoS attack</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Misuse of system resources—e.g., cryptocurrency mining</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Vandalism/ website defacement</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Phishing attack</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Software security bug</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Hardware security bug</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Emerging serious vulnerability, e.g., Meltdown/Spectre, Heartbleed</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

Sample disaster risk assessment matrix {#sample_disaster_risk_assessment_matrix}
