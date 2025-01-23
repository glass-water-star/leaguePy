from typing import Optional, List
from pydantic import BaseModel


class ThemeColors(BaseModel):
    accountNavBackground: Optional[str]
    alerts: Optional[str]
    alternateText: Optional[str]
    bodyText: Optional[str]
    buttonBackground: Optional[str]
    buttonBackgroundHover: Optional[str]
    buttonText: Optional[str]
    buttonTextHover: Optional[str]
    contentBackground: Optional[str]
    footerBackground: Optional[str]
    headerBackground: Optional[str]
    headings: Optional[str]
    links: Optional[str]
    linksHover: Optional[str]
    logo: Optional[str]
    logoBackground: Optional[str]
    mainNavBackground: Optional[str]
    mainNavLinks: Optional[str]
    mainNavLinksHover: Optional[str]
    newsletterBackground: Optional[str]
    newsletterTitle: Optional[str]
    pageBackground: Optional[str]
    sidebarBackground: Optional[str]
    widgetBackground: Optional[str]
    widgetButton: Optional[str]
    widgetButtonHover: Optional[str]
    widgetButtonLinkText: Optional[str]
    widgetButtonLinkTextHover: Optional[str]


class Theme(BaseModel):
    colors: ThemeColors


class LeagueAppSiteResponse(BaseModel):
    id: int
    name: str
    subdomain: str
    domain: Optional[str]
    timezone: str
    url: str
    logoUrl: str
    theme: Theme
