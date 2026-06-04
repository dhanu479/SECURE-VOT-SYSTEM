import asyncio
from playwright.async_api import async_playwright
import os

PAGES = {
    'home': 'http://127.0.0.1:5000/',
    'login': 'http://127.0.0.1:5000/login',
    'register': 'http://127.0.0.1:5000/register',
    'admin_login': 'http://127.0.0.1:5000/admin',
    'about': 'http://127.0.0.1:5000/about-securevote',
    'our_team': 'http://127.0.0.1:5000/our-team'
}

async def take_screenshots():
    if not os.path.exists('screenshots'):
        os.makedirs('screenshots')

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        for name, url in PAGES.items():
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
    asyncio.run(take_screenshots())
