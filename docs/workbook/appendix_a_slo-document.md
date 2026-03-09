---
title: "Example SLO Document"
book: "The Site Reliability Workbook"
part: "Appendix A"
type: "appendix"
source_url: "https://sre.google/workbook/slo-document/"
---

# Example SLO Document

This document describes the SLOs for the Example Game Service.

| Status        | Published       |
|---------------|-----------------|
| Author        | Steven Thurgood |
| Date          | 2018-02-19      |
| Reviewers     | David Ferguson  |
| Approvers     | Betsy Beyer     |
| Approval Date | 2018-02-20      |
| Revisit Date  | 2019-02-01      |

### Service Overview

The Example Game Service allows Android and iPhone users to play a game with each other. The app runs on users’ phones, and moves are sent back to the API via a REST API. The data store contains the states of all current and previous games. A score pipeline reads this table and generates up-to-date league tables for today, this week, and all time. League table results are available in the app, via the API, and also on a public HTTP server.

The SLO uses a four-week rolling window.

### SLIs and SLOs

<table id="game-service">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th>Category</th>
<th>SLI</th>
<th>SLO</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><em>API</em></p></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><p>Availability</p></td>
<td><p>The proportion of successful requests, as measured from the load balancer metrics.</p>
<p>Any HTTP status other than 500–599 is considered successful.</p>
<p><code> count of "api" http_requests which</code><br />
<code>do not have a 5XX status code</code><br />
<code>divided by</code><br />
<code>count of all "api" http_requests </code></p></td>
<td><p>97% success</p></td>
</tr>
<tr class="odd">
<td><p>Latency</p></td>
<td><p>The proportion of sufficiently fast requests, as measured from the load balancer metrics.</p>
<p>“Sufficiently fast” is defined as < 400 ms, or < 850 ms.</p>
<p><code> count of "api" http_requests with</code><br />
<code>a duration less than or equal to</code><br />
<code>"0.4" seconds</code><br />
<code>divided by</code><br />
<code>count of all "api" http_requests </code></p>
<p><code> count of "api" http_requests with</code><br />
<code>a duration less than or equal to</code><br />
<code>"0.85" seconds</code><br />
<code>divided by</code><br />
<code>count of all "api" http_requests </code></p></td>
<td><p>90% of requests < 400 ms</p>
<p>99% of requests < 850 ms</p></td>
</tr>
<tr class="even">
<td><p><em>HTTP server</em></p></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><p>Availability</p></td>
<td><p>The proportion of successful requests, as measured from the load balancer metrics.</p>
<p>Any HTTP status other than 500–599 is considered successful.</p>
<p><code> count of "web" http_requests which</code><br />
<code>do not have a 5XX status code</code><br />
<code>divided by</code><br />
<code>count of all "web" http_requests </code></p></td>
<td><p>99%</p></td>
</tr>
<tr class="even">
<td><p>Latency</p></td>
<td><p>The proportion of sufficiently fast requests, as measured from the load balancer metrics.</p>
<p>“Sufficiently fast” is defined as < 200 ms, or < 1,000 ms.</p>
<p><code> count of "web" http_requests with</code><br />
<code>a duration less than or equal to</code><br />
<code>"0.2" seconds</code><br />
<code>divided by</code><br />
<code>count of all "web" http_requests </code></p>
<p><code> count of "web" http_requests with a duration less than or equal to "1.0" seconds divided by count of all "web" http_requests </code></p></td>
<td><p>90% of requests < 200 ms</p>
<p>99% of requests < 1,000 ms</p></td>
</tr>
<tr class="odd">
<td><p><em>Score pipeline</em></p></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><p>Freshness</p></td>
<td><p>The proportion of records read from the league table that were updated recently.</p>
<p>“Recently” is defined as within 1 minute, or within 10 minutes.</p>
<p>Uses metrics from the API and HTTP server:</p>
<p><code> count of all data_requests for</code><br />
<code>"api" and "web" with freshness</code><br />
<code>less than or equal to 1 minute</code><br />
<code>divided by</code><br />
<code>count of all data_requests </code></p>
<p><code> count of all data_requests for</code><br />
<code>"api" and "web" with freshness</code><br />
<code>less than or equal to 10 minutes</code><br />
<code>divided by</code><br />
<code>count of all data_requests </code></p></td>
<td><p>90% of reads use data written within the previous 1 minute.</p>
<p>99% of reads use data written within the previous 10 minutes.</p></td>
</tr>
<tr class="odd">
<td><p>Correctness</p></td>
<td><p>The proportion of records injected into the state table by a correctness prober that result in the correct data being read from the league table.</p>
<p>A correctness prober injects synthetic data, with known correct outcomes, and exports a success metric:</p>
<p><code> count of all data_requests which</code><br />
<code>were correct</code><br />
<code>divided by</code><br />
<code>count of all data_requests </code></p></td>
<td><p>99.99999% of records injected by the prober result in the correct output.</p></td>
</tr>
<tr class="even">
<td><p>Completeness</p></td>
<td><p>The proportion of hours in which 100% of the games in the data store were processed (no records were skipped).</p>
<p>Uses metrics exported by the score pipeline:</p>
<p><code> count of all pipeline runs that</code><br />
<code>processed 100% of the records</code><br />
<code>divided by</code><br />
<code>count of all pipeline runs </code></p></td>
<td><p>99% of pipeline runs cover 100% of the data.</p></td>
</tr>
</tbody>
</table>

### Rationale

Availability and latency SLIs were based on measurement over the period 2018-01-01 to 2018-01-28. Availability SLOs were rounded down to the nearest 1% and [latency SLO](https://sre.google/workbook/implementing-slos/) timings were rounded up to the nearest 50 ms. All other numbers were picked by the author and the services were verified to be running at or above those levels.

No attempt has yet been made to verify that these numbers correlate strongly with user experience.[^1]

### Error Budget

Each objective has a separate error budget, defined as 100% minus (–) the goal for that objective. For example, if there have been 1,000,000 requests to the API server in the previous four weeks, the API availability error budget is 3% (100% – 97%) of 1,000,000: 30,000 errors.

We will enact the error budget policy (see [Example Error Budget Policy](/workbook/error-budget-policy/)) when any of our objectives has exhausted its error budget.

### Clarifications and Caveats

- Request metrics are measured at the load balancer. This measurement may fail to accurately measure cases where user requests didn’t reach the load balancer.
- We only count HTTP 5XX status messages as error codes; everything else is counted as success.
- The test data used by the correctness prober contains approximately 200 tests, which are injected every 1s. Our error budget is 48 errors every four weeks.

[^1]: Even if the numbers in the SLO are not strongly evidence-based, it is necessary to document this so that future readers can understand this fact, and make their decisions appropriately. They may decide that it is worth the investment to collect more evidence.
