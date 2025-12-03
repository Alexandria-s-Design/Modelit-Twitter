# ModelIt K12 X (Twitter) Posts - Automated Content System

Complete system for generating 104 engaging X (Twitter) posts for ModelIt K12 using AI.

## 🎯 What This Does

Generates a full year of X content (2 posts/week for 52 weeks) for ModelIt K12:
- **104 unique posts** across 8 content categories
- **Positive, engaging language** that speaks directly to teachers
- **Professional formatting** with hashtags, links, and calls-to-action
- **Ready for automation** via Google Sheets, Zapier, Make.com, or Buffer

## 📊 Content Distribution

| Category | Posts | Focus |
|----------|-------|-------|
| Feature Highlights | 20 | Platform capabilities and tools |
| Quick Wins | 15 | Fast tips and time-savers |
| Student Engagement | 15 | Transformation stories |
| Subject Integration | 15 | Cross-curricular applications |
| Teacher Testimonials | 10 | Success stories |
| Systems Thinking | 10 | 21st-century skills |
| Free Resources | 10 | Available materials |
| Positive Transformation | 9 | Exciting possibilities |

## 🚀 Quick Start

### Generate All 104 Posts

```bash
python generate_modelit_x_posts.py
```

This creates `modelit_x_posts.json` with all posts formatted and ready to use.

### Test with Sample Posts

```bash
python generate_modelit_x_posts.py test 5
```

### Upload to Google Sheets

```bash
python upload_posts_to_sheets.py modelit_x_posts.json
```

## 📁 Files

- **generate_modelit_x_posts.py** - Main generation script (uses OpenRouter + Gemini 2.5 Flash)
- **generate_modelit_x_posts_gemini.py** - Alternative using Google Gemini API directly
- **upload_posts_to_sheets.py** - Uploads generated posts to Google Sheets
- **modelit_x_posts.json** - Generated posts (104 total)
- **MODELIT-X-POSTS-PLAN.md** - Complete content strategy
- **MODELIT-X-POSTS-QUICKSTART.md** - Step-by-step usage guide
- **MODELIT-X-POSTS-COMPLETE-SUMMARY.md** - Full system documentation

## 📅 Posting Schedule

- **Mondays** - Motivational, feature highlights
- **Thursdays** - Practical tips, resources
- Starts: January 6, 2025
- Ends: December 25, 2025

## ✨ Post Structure

Each post includes:
- 2-3 engaging sentences
- 4-5 relevant hashtags (#edtech, #STEM, #teachers, etc.)
- Link to https://modelitk12.com
- Link to https://www.teacherspayteachers.com/store/modelit
- Implicit call-to-action

## 🔧 Requirements

```bash
pip install requests python-dotenv google-api-python-client google-auth-oauthlib
```

### API Keys Needed

1. **OpenRouter API Key** - Get from https://openrouter.ai
   - Add to `.env` file: `OPENROUTER_API_KEY=your_key_here`

2. **Google Sheets API** (for upload only)
   - Enable in Google Cloud Console
   - Download OAuth credentials as `credentials.json`

## 💡 Example Posts

```
Imagine your students modeling complex systems concepts collaboratively with
simple drag-and-drop tools, instantly seeing real-time visualizations come alive.
ModelIt K12 transforms abstract ideas into dynamic, interactive learning
experiences that spark genuine systems thinking.
#K12education #interactivelearning #STEM #teachertools #systemsthinking

🔗 https://modelitk12.com
📚 https://www.teacherspayteachers.com/store/modelit
```

## 🔄 Automation Options

### Zapier
```
Schedule (2x/week) → Google Sheets → X (Twitter) → Mark Posted
```

### Make.com
```
Schedule → Sheets Lookup → X Post → Update Sheet
```

### Buffer/Hootsuite
Export CSV from Google Sheet → Bulk upload → Schedule

## 📈 Success Tips

1. Monitor engagement and double down on top performers
2. Vary posting times to find optimal windows
3. Engage actively with teacher comments
4. Pin high-performing posts to profile
5. Track clicks to modelitk12.com and TPT store

## 📞 Support

For detailed usage instructions, see:
- **MODELIT-X-POSTS-QUICKSTART.md** - Step-by-step guide
- **MODELIT-X-POSTS-PLAN.md** - Strategic overview
- **MODELIT-X-POSTS-COMPLETE-SUMMARY.md** - Full documentation

---

Built with ❤️ for ModelIt K12 teachers

## Status
Active

## TODO
- [ ] Schedule upcoming posts
- [ ] Update content calendar
- [ ] Analyze engagement metrics