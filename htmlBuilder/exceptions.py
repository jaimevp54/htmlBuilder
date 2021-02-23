class HtmlBuildError(Exception):
    pass

class InvalidAttributeError(HtmlBuildError, TypeError):
    pass

class NestingError(HtmlBuildError):
    pass
