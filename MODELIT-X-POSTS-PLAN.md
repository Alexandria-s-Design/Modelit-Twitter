# ModelIt K12 X Posts Generation Plan

## Overview
Generate 104 engaging X (Twitter) posts for ModelIt K12, posted 2x per week for 1 year of content.

## Post Structure
Each post must include:
- **2-3 sentences** that engage teachers
- **Hashtags** (3-5 relevant ones)
- **Link to website**: https://modelitk12.com
- **Link to TPT store**: https://www.teacherspayteachers.com/store/modelit
- **Implicit Call-to-Action** that addresses teacher needs (engaging platform)

## Google Sheet Structure

### Column Headers:
| Column | Description | Example |
|--------|-------------|---------|
| post_number | Sequential 1-104 | 1 |
| week_number | Week of the year (1-52) | 1 |
| post_order | 1st or 2nd post of week | 1 |
| category | Type of post | Feature Highlight |
| main_text | 2-3 sentence body | Transform abstract concepts into... |
| hashtags | Space-separated tags | #edtech #STEM #systemsthinking |
| website_link | modelitk12.com | https://modelitk12.com |
| tpt_link | TPT store URL | https://www.teacherspayteachers.com/store/modelit |
| full_post | Complete formatted post | [Complete text with links] |
| scheduled_date | Optional posting date | 2025-01-06 |

## Content Strategy (Post Categories)

To create the "best and most engaging X page ever", we'll rotate through these categories:

### 1. Feature Highlights (20 posts)
- Showcase specific ModelIt K12 features
- How each feature makes teaching easier
- Real classroom applications

### 2. Quick Wins (15 posts)
- "Did you know..." facts
- Time-saving tips
- Simple strategies teachers can use immediately

### 3. Student Engagement Stories (15 posts)
- How students react to interactive modeling
- "Aha!" moments
- Engagement transformations

### 4. Subject Integration (15 posts)
- Science applications
- Math connections
- Cross-curricular uses
- Standards alignment (NGSS, state standards)

### 5. Teacher Testimonials/Social Proof (10 posts)
- Success stories (can be hypothetical but realistic)
- Community impact
- Classroom transformations

### 6. Systems Thinking Benefits (10 posts)
- Why systems thinking matters
- 21st-century skills
- Critical thinking development

### 7. Free Resources (10 posts)
- Available free materials
- Getting started guides
- Sample lessons

### 8. Problem-Solution Posts (9 posts)
- Common teaching challenges
- How ModelIt K12 solves them
- Before/after scenarios

## JSON Schema for Automation

```json
{
  "posts": [
    {
      "post_number": 1,
      "week_number": 1,
      "post_order": 1,
      "category": "Feature Highlight",
      "main_text": "Watch your students' eyes light up as abstract concepts come alive through interactive modeling. ModelIt K12 transforms passive learning into active exploration, making complex systems thinking accessible and engaging.",
      "hashtags": "#edtech #STEM #systemsthinking #teacherresources #K12education",
      "website_link": "https://modelitk12.com",
      "tpt_link": "https://www.teacherspayteachers.com/store/modelit",
      "full_post": "Watch your students' eyes light up as abstract concepts come alive through interactive modeling. ModelIt K12 transforms passive learning into active exploration, making complex systems thinking accessible and engaging. #edtech #STEM #systemsthinking #teacherresources #K12education\n\n🔗 https://modelitk12.com\n📚 https://www.teacherspayteachers.com/store/modelit",
      "scheduled_date": "2025-01-06"
    }
  ]
}
```

## Technical Implementation

### Tools & APIs:
- **OpenRouter API** with Nano Banana (google/gemini-flash-2.5-exp)
- **Python** for generation script
- **Google Sheets API** for upload
- **JSON** output format for automation

### Script Flow:
1. Load content strategy and prompt templates
2. For each of 104 posts:
   - Select category based on distribution
   - Generate post using OpenRouter + Nano Banana
   - Ensure all required elements present
   - Format for X character limits
   - Structure in JSON format
3. Save to JSON file
4. Upload to Google Sheet

### Prompt Engineering for Nano Banana:
Each prompt will include:
- Specific category guidance
- Teacher pain points (need for engagement)
- Tone: enthusiastic, supportive, solution-focused
- Character limits for X (280 chars for main text, room for links)
- Requirements: 2-3 sentences, implicit CTA, natural flow

## Hashtag Strategy
Mix of:
- Broad reach: #edtech #teachers #K12education
- Specific: #STEM #systemsthinking #scienceteacher
- Trending: #edchat #teachertwitter #iteachscience
- Seasonal: #backtoschool #endofyear (where appropriate)

## Distribution Schedule
- **Monday** posts: Motivational, feature highlights, inspirational
- **Thursday** posts: Practical tips, quick wins, resources

## Success Metrics to Track
- Engagement rate
- Link clicks to website
- TPT store visits
- Most engaging categories
- Best performing hashtags

## Next Steps
1. ✅ Complete plan design
2. ⏳ Build Python generation script
3. ⏳ Test with 5-10 posts
4. ⏳ Generate all 104 posts
5. ⏳ Create Google Sheet
6. ⏳ Set up automation workflow
