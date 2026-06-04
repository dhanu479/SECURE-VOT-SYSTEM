import asyncio
from playwright.async_api import async_playwright
import os

AUTH_PAGES = {
    'face_verify': 'http://127.0.0.1:5000/face-verify',
    'vote': 'http://127.0.0.1:5000/vote',
    'result': 'http://127.0.0.1:5000/result',
    'admin_dashboard': 'http://127.0.0.1:5000/admin/dashboard'
}

async def take_auth_screenshots():
    if not os.path.exists('screenshots'):
        os.makedirs('screenshots')

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context()
        page = await context.new_page()
        
        # First hit the mock session endpoint to log in
        print("Authenticating with mock session...")
        await page.goto('http://127.0.0.1:5000/mock-session')
        
        for name, url in AUTH_PAGES.items():
            print(f"Taking screenshot of {name} at {url}...")
            try:
                await page.goto(url)
                # wait a bit for animations or assets to load
                await page.wait_for_timeout(1000)
                await page.screenshot(path=f'screenshots/{name}.png', full_page=True)
                print(f"Saved screenshots/{name}.png")
            except Exception as e:
                print(f"Failed to capture {name}: {e}")
        
        await browser.close()

if __name__ == '__main__':
    asyncio.run(take_auth_screenshots())
