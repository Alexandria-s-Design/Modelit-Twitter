# ModelIt K12 X Posts - Quick Start Guide

## 🎯 Overview
This system generates 104 engaging X (Twitter) posts for ModelIt K12 using AI, then uploads them to Google Sheets for easy automation.

## 📋 What You Get
- **104 unique posts** (2 per week for 52 weeks)
- **8 content categories** rotating for variety and engagement
- **JSON format** ready for automation tools
- **Google Sheet** with all posts organized and scheduled
- **Professional formatting** with hashtags, links, and CTAs

## 🚀 Quick Start

### Step 1: Test Generation (5 posts)
```bash
cd C:\Users\MarieLexisDad\scripts
python generate_modelit_x_posts.py test 5
```

This will:
- Generate 5 sample posts
- Show you the output format
- Verify your OpenRouter API key works
- Let you review before generating all 104

### Step 2: Generate All 104 Posts
```bash
python generate_modelit_x_posts.py
```

This will:
- Generate all 104 posts
- Save to `modelit_x_posts.json`
- Take ~10-15 minutes
- Create batches of 10 posts with periodic saves

### Step 3: Upload to Google Sheets
```bash
python upload_posts_to_sheets.py modelit_x_posts.json
```

This will:
- Create a new Google Sheet
- Format with headers and styling
- Upload all 104 posts
- Give you a shareable link

## 📊 Output Format

### JSON Structure
```json
{
  "metadata": {
    "total_posts": 104,
    "generated_at": "2025-01-21T...",
    "model": "google/gemini-flash-2.5-exp",
    "start_date": "2025-01-06"
  },
  "posts": [
    {
      "post_number": 1,
      "week_number": 1,
      "post_order": 1,
      "category": "Feature Highlight",
      "main_text": "...",
      "hashtags": "...",
      "website_link": "https://modelitk12.com",
      "tpt_link": "https://www.teacherspayteachers.com/store/modelit",
      "full_post": "...",
      "scheduled_date": "2025-01-06"
    }
  ]
}
```

### Google Sheet Columns
| Column | Description |
|--------|-------------|
| Post # | Sequential number 1-104 |
| Week # | Week of year (1-52) |
| Post Order | 1st or 2nd post of week |
| Category | Content type |
| Main Text | 2-3 sentence body |
| Hashtags | 4-5 relevant tags |
| Website Link | modelitk12.com |
| TPT Link | TeachersPayTeachers store |
| Full Post | Complete formatted post |
| Scheduled Date | Suggested posting date |

## 🎨 Content Categories (104 posts total)

1. **Feature Highlights** (20) - Showcase platform capabilities
2. **Quick Wins** (15) - Fast tips and tricks
3. **Student Engagement** (15) - Transformation stories
4. **Subject Integration** (15) - Cross-curricular applications
5. **Teacher Testimonials** (10) - Success stories
6. **Systems Thinking** (10) - Skills development
7. **Free Resources** (10) - Available materials
8. **Problem-Solution** (9) - Before/after scenarios

## 📅 Posting Schedule
- **Mondays**: Motivational, feature highlights
- **Thursdays**: Practical tips, resources
- Starts: January 6, 2025
- Ends: December 25, 2025

## 🔧 Requirements

### Environment Variables
Create/update `.env` file:
```
OPENROUTER_API_KEY=your_key_here
```

### Python Packages
```bash
pip install requests python-dotenv google-api-python-client google-auth-oauthlib google-auth-httplib2
```

### Google Sheets API Setup
1. Go to [Google Cloud Console](https://console.cloud.google.com)
2. Create a new project (or use existing)
3. Enable Google Sheets API
4. Create OAuth 2.0 credentials
5. Download as `credentials.json`
6. Place in `scripts/` folder

## 🎯 Next Steps After Upload

### 1. Review & Edit
- Read through posts
- Tweak any that need refinement
- Adjust scheduled dates
- Add seasonal variations

### 2. Set Up Automation
Choose one:
- **Zapier**: Google Sheets → X (Twitter)
- **Make.com**: Schedule + post automation
- **Buffer**: Bulk upload CSV
- **Hootsuite**: Import from Google Sheets

### 3. Monitor & Optimize
Track:
- Engagement rates (likes, retweets, comments)
- Link clicks to modelitk12.com
- TPT store visits
- Best performing categories
- Top hashtags

### 4. Iterate
- Double down on what works
- Create variations of top posts
- Adjust posting times
- Test different hashtag combinations

## 🔄 Regenerating Specific Posts

If you want to regenerate specific posts:

1. Edit `generate_modelit_x_posts.py`
2. Modify the range in the main loop
3. Run with specific post numbers

Or simply edit directly in the Google Sheet!

## 📈 Automation Examples

### Example: Zapier Flow
```
Trigger: Schedule by Zapier (twice weekly)
↓
Action: Google Sheets (Get Row)
↓
Filter: Where Post Order = 1 (Mondays) or 2 (Thursdays)
↓
Action: X (Twitter) - Create Tweet
```

### Example: Make.com Scenario
```
Schedule → Google Sheets Lookup → X Post → Update Row (Mark as Posted)
```

## 💡 Pro Tips

1. **Vary posting times** to find optimal engagement
2. **Monitor trending hashtags** and swap them in
3. **Create urgency** around TPT sales and promotions
4. **Engage back** when teachers comment or ask questions
5. **Pin top performers** to your profile
6. **Save high-engagement posts** to use again in 6 months
7. **A/B test** different CTA styles

## 🆘 Troubleshooting

### "API key not found"
- Check `.env` file exists in scripts folder
- Verify `OPENROUTER_API_KEY=...` is set

### "Google auth failed"
- Ensure `credentials.json` is in scripts folder
- Delete `token.json` and re-authenticate

### "Rate limit exceeded"
- Script has built-in delays (1 sec between posts)
- If needed, increase sleep time in code

### Posts seem off-topic
- Review category prompts in code
- Adjust temperature (currently 0.8)
- Regenerate specific categories

## 📞 Support
Questions? Issues? Want to customize?
- Review the detailed plan: `MODELIT-X-POSTS-PLAN.md`
- Check the code comments
- Test with small batches first

---

## 🎉 You're Ready!

Run the test, review the output, then generate all 104 posts. You'll have a full year of engaging content ready to go!
