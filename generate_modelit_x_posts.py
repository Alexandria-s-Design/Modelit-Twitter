"""
Generate 104 engaging X posts for ModelIt K12 using OpenRouter + Nano Banana (Gemini Flash 2.5)
Outputs to JSON format for Google Sheets automation
"""

import os
import json
import time
from datetime import datetime, timedelta
from typing import List, Dict
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv(override=True)

# Configuration
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
MODEL = "google/gemini-2.5-flash-preview-09-2025"  # Nano Banana (Gemini 2.5 Flash)
WEBSITE_URL = "https://modelitk12.com"
TPT_URL = "https://www.teacherspayteachers.com/store/modelit"

# Content categories with distribution
CATEGORIES = {
    "Feature Highlight": 20,
    "Quick Win": 15,
    "Student Engagement": 15,
    "Subject Integration": 15,
    "Teacher Testimonial": 10,
    "Systems Thinking": 10,
    "Free Resources": 10,
    "Problem Solution": 9
}

# Start date for scheduling (first Monday)
START_DATE = datetime(2025, 1, 6)  # Adjust as needed

def create_category_distribution() -> List[str]:
    """Create a list of 104 categories based on distribution"""
    categories = []
    for category, count in CATEGORIES.items():
        categories.extend([category] * count)
    return categories

def get_category_prompt(category: str, post_num: int) -> str:
    """Generate specific prompt based on category"""

    base_context = """You are creating an engaging X (Twitter) post for ModelIt K12, an interactive modeling platform that helps teachers make abstract concepts concrete and engaging for students.

Your audience: K-12 teachers who want to create more engaging, interactive learning experiences for their students.

REQUIREMENTS:
- Exactly 2-3 sentences (no more, no less)
- Natural, conversational tone that speaks directly to teachers
- Include an implicit call-to-action (make them want to learn more)
- Stay under 200 characters for the main text (we'll add hashtags and links separately)
- Use POSITIVE, aspirational language - focus on possibilities, not problems
- NEVER use negative phrases like "tired of", "struggling", "frustrated", "stop doing"
- Be specific and authentic, not generic marketing speak
- Highlight the exciting outcomes and possibilities

"""

    category_guidance = {
        "Feature Highlight": """CATEGORY: Feature Highlight
Showcase a specific ModelIt K12 feature and how it transforms teaching. Focus on:
- Interactive modeling capabilities
- Real-time visualization
- Student collaboration features
- Drag-and-drop simplicity
- Systems thinking tools

Make the teacher envision using this in their classroom tomorrow.""",

        "Quick Win": """CATEGORY: Quick Win
Share a fast, actionable tip or "did you know" fact. Focus on:
- Time-saving shortcuts
- Simple strategies for immediate use
- Surprising benefits they didn't know about
- 5-minute implementation ideas

Keep it snappy and valuable.""",

        "Student Engagement": """CATEGORY: Student Engagement Story
Paint a picture of student excitement and discovery. Focus on:
- "Aha!" moments when concepts click
- Students getting genuinely excited about learning
- Students asking to do more modeling
- Peer teaching and collaboration

Make it emotional, positive, and relatable.""",

        "Subject Integration": """CATEGORY: Subject Integration
Show how ModelIt K12 works across subjects. Focus on:
- STEM applications (ecosystems, chemical reactions, physics)
- Math modeling and data visualization
- Cross-curricular connections
- Standards alignment (NGSS, state standards)

Be specific about grade levels and topics.""",

        "Teacher Testimonial": """CATEGORY: Teacher Testimonial
Share a realistic success story (can be composite/hypothetical but authentic). Focus on:
- What the teacher wanted to achieve
- How ModelIt K12 helped them succeed
- Measurable positive impact (engagement, understanding, enjoyment)

Use first-person perspective or quote format with enthusiastic, positive tone.""",

        "Systems Thinking": """CATEGORY: Systems Thinking Benefits
Explain why systems thinking matters for students. Focus on:
- 21st-century skills development
- Critical thinking and problem-solving
- Real-world application preparation
- Cause-and-effect understanding

Connect to future readiness.""",

        "Free Resources": """CATEGORY: Free Resources
Highlight available free materials. Focus on:
- Ready-to-use lesson plans
- Sample models to try
- Getting started guides
- No-cost trial options

Emphasize "try it now" accessibility.""",

        "Problem Solution": """CATEGORY: Positive Transformation
Showcase how ModelIt K12 creates exciting new possibilities for teaching. Focus on:
- Making abstract concepts come alive for students
- Access to powerful interactive tools
- Ready-to-use engaging lessons
- Easy differentiation opportunities

Use positive "imagine...", "discover...", "unlock..." language that inspires action."""
    }

    return base_context + category_guidance.get(category, "")

def generate_hashtags(category: str, variation: int) -> str:
    """Generate relevant hashtags based on category"""

    # Core hashtags (always include 1-2)
    core = ["#edtech", "#K12education", "#teachers"]

    # Category-specific hashtags
    category_tags = {
        "Feature Highlight": ["#STEM", "#systemsthinking", "#interactivelearning", "#teachertools"],
        "Quick Win": ["#teachertips", "#edchat", "#teacherlife", "#classroomhacks"],
        "Student Engagement": ["#studentengagement", "#teacherwin", "#education", "#engagedlearning"],
        "Subject Integration": ["#scienceteacher", "#STEMeducation", "#NGSScience", "#iteachscience"],
        "Teacher Testimonial": ["#teacherstories", "#eduwin", "#teachercommunity", "#edchat"],
        "Systems Thinking": ["#criticalthinking", "#21stcenturyskills", "#deeplearning", "#STEM"],
        "Free Resources": ["#teacherresources", "#freebies", "#teachersfollowteachers", "#iteach"],
        "Problem Solution": ["#teacherproblems", "#edtech", "#classroomsolutions", "#teachingtools"]
    }

    # Select 4-5 hashtags: 1 core + 3-4 category-specific
    import random
    selected = [core[variation % len(core)]]
    cat_tags = category_tags.get(category, ["#education", "#teaching"])
    selected.extend(random.sample(cat_tags, min(4, len(cat_tags))))

    return " ".join(selected[:5])

def call_openrouter(prompt: str, max_retries: int = 3) -> str:
    """Call OpenRouter API with Nano Banana model"""

    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://modelitk12.com",
        "X-Title": "ModelIt K12 Content Generator"
    }

    payload = {
        "model": MODEL,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0.8,
        "max_tokens": 200
    }

    for attempt in range(max_retries):
        try:
            response = requests.post(url, headers=headers, json=payload, timeout=30)
            response.raise_for_status()

            result = response.json()
            content = result['choices'][0]['message']['content'].strip()
            return content

        except requests.exceptions.RequestException as e:
            print(f"  ⚠️  Attempt {attempt + 1} failed: {e}")
            if attempt < max_retries - 1:
                time.sleep(2 ** attempt)  # Exponential backoff
            else:
                raise

    return ""

def create_full_post(main_text: str, hashtags: str) -> str:
    """Combine all elements into final X post format"""
    return f"""{main_text} {hashtags}

🔗 {WEBSITE_URL}
📚 {TPT_URL}"""

def generate_post(category: str, post_num: int, week_num: int, post_order: int) -> Dict:
    """Generate a single X post"""

    print(f"  Generating post {post_num}/104 - {category}...")

    # Create prompt
    prompt = get_category_prompt(category, post_num)
    prompt += f"\n\nGenerate post #{post_num}. Return ONLY the 2-3 sentence post text, nothing else."

    # Generate main text
    main_text = call_openrouter(prompt)

    # Clean up any extra formatting
    main_text = main_text.strip().strip('"').strip("'")

    # Generate hashtags
    hashtags = generate_hashtags(category, post_num)

    # Calculate scheduled date (Monday or Thursday)
    days_offset = (week_num - 1) * 7 + (0 if post_order == 1 else 3)
    scheduled_date = (START_DATE + timedelta(days=days_offset)).strftime("%Y-%m-%d")

    # Create full post
    full_post = create_full_post(main_text, hashtags)

    return {
        "post_number": post_num,
        "week_number": week_num,
        "post_order": post_order,
        "category": category,
        "main_text": main_text,
        "hashtags": hashtags,
        "website_link": WEBSITE_URL,
        "tpt_link": TPT_URL,
        "full_post": full_post,
        "scheduled_date": scheduled_date
    }

def generate_all_posts(output_file: str = "modelit_x_posts.json", batch_size: int = 10):
    """Generate all 104 posts"""

    print("🚀 Starting ModelIt K12 X Posts Generation")
    print(f"📊 Using model: {MODEL}")
    print(f"📅 Starting from: {START_DATE.strftime('%Y-%m-%d')}")
    print(f"💾 Output file: {output_file}\n")

    # Create category distribution
    categories = create_category_distribution()

    posts = []

    # Generate posts
    for i in range(104):
        post_num = i + 1
        week_num = (i // 2) + 1
        post_order = (i % 2) + 1
        category = categories[i]

        try:
            post = generate_post(category, post_num, week_num, post_order)
            posts.append(post)

            # Save periodically
            if post_num % batch_size == 0:
                save_posts(posts, output_file)
                print(f"  ✅ Saved batch at post {post_num}\n")

            # Rate limiting (be nice to the API)
            time.sleep(1)

        except Exception as e:
            print(f"  ❌ Error generating post {post_num}: {e}")
            # Create a placeholder
            posts.append({
                "post_number": post_num,
                "week_number": week_num,
                "post_order": post_order,
                "category": category,
                "main_text": "ERROR - Manual review needed",
                "hashtags": "",
                "website_link": WEBSITE_URL,
                "tpt_link": TPT_URL,
                "full_post": "ERROR - Manual review needed",
                "scheduled_date": ""
            })

    # Final save
    save_posts(posts, output_file)

    print(f"\n✨ Generation complete!")
    print(f"📝 Total posts: {len(posts)}")
    print(f"💾 Saved to: {output_file}")

    # Print summary
    print_summary(posts)

    return posts

def save_posts(posts: List[Dict], filename: str):
    """Save posts to JSON file"""
    output = {
        "metadata": {
            "total_posts": len(posts),
            "generated_at": datetime.now().isoformat(),
            "model": MODEL,
            "website_url": WEBSITE_URL,
            "tpt_url": TPT_URL,
            "start_date": START_DATE.strftime("%Y-%m-%d")
        },
        "posts": posts
    }

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

def print_summary(posts: List[Dict]):
    """Print generation summary"""
    from collections import Counter

    print("\n" + "="*50)
    print("📊 GENERATION SUMMARY")
    print("="*50)

    # Count by category
    categories = Counter(p['category'] for p in posts)
    print("\nPosts by Category:")
    for cat, count in sorted(categories.items()):
        print(f"  {cat}: {count}")

    # Sample posts
    print("\n📝 Sample Posts (first 3):")
    for i, post in enumerate(posts[:3], 1):
        print(f"\n--- Post {i} ({post['category']}) ---")
        print(post['full_post'])

def test_generation(num_posts: int = 5):
    """Test generation with a small batch"""
    print(f"🧪 Testing with {num_posts} posts...\n")

    categories = create_category_distribution()[:num_posts]

    for i in range(num_posts):
        post_num = i + 1
        week_num = (i // 2) + 1
        post_order = (i % 2) + 1
        category = categories[i]

        post = generate_post(category, post_num, week_num, post_order)

        print(f"\n{'='*60}")
        print(f"POST {post_num} - {category}")
        print('='*60)
        print(post['full_post'])
        print()

        time.sleep(1)

if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "test":
        # Test mode
        num_test = int(sys.argv[2]) if len(sys.argv) > 2 else 5
        test_generation(num_test)
    else:
        # Full generation
        output_file = sys.argv[1] if len(sys.argv) > 1 else "modelit_x_posts.json"
        generate_all_posts(output_file)
