![banner](https://github.com/PJURC-data-analysis/podcasts-reviews/blob/main/media/banner.png)

# Podcast Market Analysis: Optimizing Category Selection
[View Notebook](https://github.com/PJURC-data-analysis/podcasts-reviews/blob/main/Podcasts%20Reviews.ipynb)

A statistical analysis of iTunes podcast ratings and reviews to identify optimal category selection for a new business-focused podcast. This study uses hypothesis testing to compare business and technology categories, examining ratings, review patterns, and subcategory performance.

## Overview

### Business Question 
Which podcast category (business or technology) offers better potential for a new podcast focused on process automation and business analysis?

### Key Findings
- Business podcasts average 4.85 rating vs 4.52-4.54 for technology
- Business podcasts receive 19-20 reviews vs 13-17 for technology
- Both categories show weak negative rating-review count correlation
- Marketing subcategory has highest ratings in business category
- Single-review podcasts significantly impact rating distributions

### Impact/Results
- Identified optimal podcast category
- Established rating benchmarks
- Quantified review patterns
- Validated category selection
- Created subcategory performance metrics

## Data

### Source Information
- Dataset: iTunes podcast reviews and ratings
- Source: Kaggle Dataset
- Coverage: All iTunes podcasts and reviews

### Variables Analyzed
- Podcast categories
- Rating scores
- Review counts
- Subcategories
- Category correlations
- Statistical relationships

## Methods

### Analysis Approach
1. Hypothesis Testing
   - Mean rating differences
   - Review count differences
   - Rating-review correlations
2. Confidence Intervals
   - Category comparisons
   - Rating distributions
   - Review patterns
3. Subcategory Analysis
   - Performance metrics
   - Rating variations

### Tools Used

- Python (Data Analysis)
  - Pandas: Data manipulation
  - Numpy: Numerical computations
  - Matplotlib: Visualization
  - Seaborn: Visualization
  - Plotly: Visualization
  - Sqlite: Data Querying
  - Scipy: Inferential Statistics
  - Statsmodels: Inferential Statistics
- Microsoft PowerBI (Interactive Data Visualization)

## Getting Started

### Prerequisites
```python
ipython==8.12.3
numpy==2.2.0
pandas==2.2.3
scipy==1.14.1
seaborn==0.13.2
matplotlib==3.8.4
scipy==1.14.1
statsmodels==0.14.4
```

### Installation & Usage
```bash
git clone git@github.com:PJURC-data-analysis/podcasts-reviews.git
cd tech-mental-health
pip install -r requirements.txt
jupyter notebook "Tech Mental Health.ipynb"
```

Download the dataset from [Kaggle](https://www.kaggle.com/datasets/thoughtvector/podcastreviews) unzip it to the working directory, `archive` folder.

The `podcasts.pbix` report can be opened through Microsoft Power BI.

## Project Structure
podcasts-reviews/
│   README.md
│   requirements.txt
│   Podcasts Reviews.ipynb
|   utils.py
|   podcasts.pbix
└── archive/
    └── database.sqlite

## Strategic Recommendations
1. **Category Selection**
   - Focus on business category
   - Target business automation niche
   - Leverage professional experience
   - Consider subcategory positioning

2. **Content Strategy**
   - Emphasize professional expertise
   - Focus on automation topics
   - Maintain quality for ratings
   - Build review engagement

3. **Performance Metrics**
   - Target 4.85+ rating
   - Build review base
   - Monitor subcategory trends
   - Track engagement patterns

## Future Improvements
- Exclude single-review analysis
- Add temporal analysis
- Include review text analysis
- Expand platform coverage
- Compare cross-platform data
- Analyze listener demographics