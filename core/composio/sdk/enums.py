from enum import Enum

class App(Enum):
    CLICKUP = "clickup"
    GOOGLE_DRIVE = "google-drive"
    GOOGLE_SHEETS = "google-sheets"
    CALENDLY = "calendly"
    ZENDESK = "zendesk"
    ASANA = "asana"
    GITHUB = "github"
    JIRA = "jira"
    SLACK = "slack"
    TRELLO = "trello"
    GOOGLE_CALENDAR = "google-calendar"
    GOOGLE_DOCS = "google-docs"
    LINEAR = "linear"
    NOTION = "notion"
    DROPBOX = "dropbox"
    MIXPANEL = "mixpanel"
    MONDAY = "monday"
    BITBUCKET = "bitbucket"
    STRAVA = "strava"
    INTERCOM = "intercom"
    FIGMA = "figma"
    KEAP = "keap"
    KLAVIYO = "klaviyo"
    MAILCHIMP = "mailchimp"
    GUMROAD = "gumroad"
    DISCORD = "discord"
    ZOOM = "zoom"
    TASKADE = "taskade"
    TYPEFORM = "typeform"
    TIMELY = "timely"
    TODOIST = "todoist"
    TWITCH = "twitch"
    BOX = "box"
    ZOHO = "zoho"
    ATTIO = "attio"
    SURVEY_MONKEY = "survey-monkey"
    STACK_EXCHANGE = "stack-exchange"
    PIPEDRIVE = "pipedrive"
    PAGERDUTY = "pagerduty"
    FRESHDESK = "freshdesk"
    HUBSPOT = "hubspot"
    EVENTBRITE = "eventbrite"
    GITLAB = "gitlab"
    SHOPIFY = "shopify"
    MIRO = "miro"
    SPLITWISE = "splitwise"

class TestIntegration(Enum):
    CLICKUP = "test-clickup-connector"
    GOOGLE_DRIVE = "test-google-drive-connector"
    GOOGLE_SHEETS = "test-google-sheets-connector"
    CALENDLY = "test-calendly-connector"
    ZENDESK = "test-zendesk-connector"
    ASANA = "test-asana-connector"
    GITHUB = "test-github-connector"
    JIRA = "test-jira-connector"
    SLACK = "test-slack-connector"
    TRELLO = "test-trello-connector"
    GOOGLE_CALENDAR = "test-google-calendar-connector"
    GOOGLE_DOCS = "test-google-docs-connector"
    LINEAR = "test-linear-connector"
    NOTION = "test-notion-connector"
    DROPBOX = "test-dropbox-connector"
    MIXPANEL = "test-mixpanel-connector"
    MONDAY = "test-monday-connector"
    BITBUCKET = "test-bitbucket-connector"
    STRAVA = "test-strava-connector"
    INTERCOM = "test-intercom-connector"
    FIGMA = "test-figma-connector"
    KEAP = "test-keap-connector"
    KLAVIYO = "test-klaviyo-connector"
    MAILCHIMP = "test-mailchimp-connector"
    GUMROAD = "test-gumroad-connector"
    DISCORD = "test-discord-connector"
    ZOOM = "test-zoom-connector"
    TASKADE = "test-taskade-connector"
    TYPEFORM = "test-typeform-connector"
    TIMELY = "test-timely-connector"
    TODOIST = "test-todoist-connector"
    TWITCH = "test-twitch-connector"
    BOX = "test-box-connector"
    ZOHO = "test-zoho-connector"
    ATTIO = "test-attio-connector"
    SURVEY_MONKEY = "test-survey-monkey-connector"
    STACK_EXCHANGE = "test-stack-exchange-connector"
    PIPEDRIVE = "test-pipedrive-connector"
    PAGERDUTY = "test-pagerduty-connector"
    FRESHDESK = "test-freshdesk-connector"
    HUBSPOT = "test-hubspot-connector"
    EVENTBRITE = "test-eventbrite-connector"
    GITLAB = "test-gitlab-connector"
    SHOPIFY = "test-shopify-connector"
    MIRO = "test-miro-connector"
    SPLITWISE = "test-splitwise-connector"

class Action(Enum):
    def __init__(self, service, action):
        self.service = service
        self.action = action

    CLICKUP_CREATE_TASK = ("clickup", "clickup_create_task")
    CLICKUP_GET_TASKS = ("clickup", "clickup_get_tasks")
    CLICKUP_GET_TASK = ("clickup", "clickup_get_task")
    CLICKUP_CREATE_LIST = ("clickup", "clickup_create_list")
    CLICKUP_GET_LISTS = ("clickup", "clickup_get_lists")
    CLICKUP_GET_SPACES = ("clickup", "clickup_get_spaces")
    CLICKUP_CREATE_SPACE = ("clickup", "clickup_create_space")
    CLICKUP_CREATE_FOLDER = ("clickup", "clickup_create_folder")
    CLICKUP_GET_FOLDERS = ("clickup", "clickup_get_folders")
    ZENDESK_CREATE_ZENDESK_ORGANIZATION = ("zendesk", "zendesk_create_zendesk_organization")
    ZENDESK_DELETE_ZENDESK_ORGANIZATION = ("zendesk", "zendesk_delete_zendesk_organization")
    ZENDESK_COUNT_ZENDESK_ORGANIZATIONS = ("zendesk", "zendesk_count_zendesk_organizations")
    ZENDESK_GET_ZENDESK_ORGANIZATION = ("zendesk", "zendesk_get_zendesk_organization")
    ZENDESK_GET_ZENDESK_ORGANIZATIONS = ("zendesk", "zendesk_get_all_zendesk_organizations")
    ZENDESK_UPDATE_ZENDESK_ORGANIZATION = ("zendesk", "zendesk_update_zendesk_organization")
    ZENDESK_CREATE_ZENDESK_TICKET = ("zendesk", "zendesk_create_zendesk_ticket")
    ZENDESK_DELETE_ZENDESK_TICKET = ("zendesk", "zendesk_delete_zendesk_ticket")
    ZENDESK_GET_ZENDESK_ABOUT_ME = ("zendesk", "zendesk_get_about_me")
    ASANA_CREATE_SUBTASK = ("asana", "asana_create_subtask")
    ASANA_GET_SUBTASKS = ("asana", "asana_get_subtasks")
    GITHUB_CREATE_ISSUE = ("github", "github_create_issue")
    GITHUB_GET_REPOSITORY = ("github", "github_list_github_repos")
    GITHUB_STAR_REPO = ("github", "github_star_repo")
    GITHUB_GET_ABOUT_ME = ("github", "github_get_about_me")
    GITHUB_FETCH_README = ("github", "github_fetch_readme")
    GITHUB_GET_COMMITS = ("github", "github_get_commits")
    GITHUB_GET_COMMITS_WITH_PATCH_FILE_FOR_THAT_COMMIT = ("github", "github_get_commits_with_code")
    GITHUB_GET_PATCH_FOR_COMMIT = ("github", "github_get_patch_for_commit")
    TRELLO_CREATE_TRELLO_LIST = ("trello", "trello_create_trello_list")
    TRELLO_CREATE_TRELLO_CARD = ("trello", "trello_create_trello_card")
    TRELLO_GET_TRELLO_BOARD_CARDS = ("trello", "trello_get_trello_board_cards")
    TRELLO_DELETE_TRELLO_CARD = ("trello", "trello_delete_trello_card")
    TRELLO_ADD_TRELLO_CARD_COMMENT = ("trello", "trello_add_trello_card_comment")
    TRELLO_CREATE_TRELLO_LABEL = ("trello", "trello_create_trello_label")
    TRELLO_UPDATE_TRELLO_BOARD = ("trello", "trello_update_trello_board")
    TRELLO_GET_ABOUT_ME = ("trello", "trello_get_about_me")
    LINEAR_CREATE_ISSUE = ("linear", "linear_create_linear_issue")
    LINEAR_GET_PROJECTS = ("linear", "linear_list_linear_projects")
    LINEAR_GET_TEAMS_BY_PROJECT = ("linear", "linear_list_linear_teams")
    NOTION_CREATE_NOTION_DATABASE = ("notion", "notion_create_notion_database")
    NOTION_CREATE_NOTION_PAGE = ("notion", "notion_create_notion_page")
    NOTION_FETCH_NOTION_PAGE = ("notion", "notion_fetch_notion_page")
    NOTION_ARCHIVE_NOTION_PAGE = ("notion", "notion_archive_notion_page")
    NOTION_FETCH_NOTION_DATABASE = ("notion", "notion_fetch_notion_database")
    NOTION_UPDATE_NOTION_DATABASE = ("notion", "notion_update_notion_database")
    NOTION_CREATE_PAGE_COMMENT = ("notion", "notion_create_page_comment")
    NOTION_GET_ABOUT_ME = ("notion", "notion_get_about_me")
    DROPBOX_GET_ABOUT_ME = ("dropbox", "dropbox_get_about_me")
    TYPEFORM_GET_ABOUT_ME = ("typeform", "typeform_get_about_me")

class Trigger(Enum):
    def __init__(self, service, trigger):
        self.service = service
        self.trigger = trigger

    GITHUB_PULL_REQUEST_EVENT = ("github", "github_pull_request_event")
    GITHUB_COMMIT_EVENT = ("github", "github_commit_event")
    SLACK_NEW_MESSAGE = ("slack", "slack_receive_message")
