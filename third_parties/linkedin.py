import os
import requests
from dotenv import load_dotenv
from typing import Optional, Dict, Any

load_dotenv()


def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = True) -> Optional[Dict[str, Any]]:
    """
    Scrape the LinkedIn profile URL and return the profile data.
    - When mock=True (default), fetches a public JSON from a gist for local dev/testing.
    - When mock=False, raises NotImplementedError (placeholder for real implementation).
    """
    if mock:
        mock_url = (
            "https://gist.githubusercontent.com/KhanAhmedRaza/50c61ea04efd9ecd3224f289f6569606/"
            "raw/567d9d78c36a3eb360863bb752e903f5834e8171/ahmed-linkedin.json"
        )
        try:
            resp = requests.get(mock_url, timeout=15)
            resp.raise_for_status()
            payload = resp.json()
            # Some mocks may wrap content under "person"; fall back to payload itself
            return payload.get("person") if isinstance(payload, dict) else payload
        except Exception as exc:
            print(f"Mock fetch failed: {exc}")
            return None
    else:
        # Placeholder: Real LinkedIn scraping typically requires a third‑party API or authenticated session
        # due to LinkedIn's protections. Consider integrating a provider and using an API key from .env.
        raise NotImplementedError("Real LinkedIn scraping not implemented. Use mock=True for testing.")


if __name__ == "__main__":
    data = scrape_linkedin_profile("https://www.linkedin.com/in/khanahmedraza/", mock=True)
    print(data)






