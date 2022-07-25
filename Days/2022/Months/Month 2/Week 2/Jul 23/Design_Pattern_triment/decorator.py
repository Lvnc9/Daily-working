#!/usr/bin/python
# Start
# Decorators
# Modules
from email.mime import application
import functools
from html import escape
from gpg import Data


def float_args_and_return(function):
    # to set __name__ to the origin one
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        args = [float[arg] for arg in args]
        return float(function(*args, **kwargs))

    return wrapper


def statically_typed(*types, return_type=None):
    def decorator(function):
        @functools.wraps
        def wrapper(*args, **kwargs):
            if len(args) > len(types):
                raise ValueError('To many arguments')
            elif len(args) < len(types):
                raise ValueError('to few arguements')
            for i, (arg, type_) in enumerate(zip(args, types)):
                if not isinstance(arg, type_):
                    raise ValueError(
                        f"argument {arg} must be a type of {type_.__name__}")
            result = function(*args, **kwargs)

            if (return_type is not None and 
                not isinstance(result, return_type)):
                raise ValueError(f"return value must be of type{return_type.__name__}")
            return result
        return wrapper
    return decorator

class Web: 
    pass

class bottle : 
    pass

def secret():
    pass

def COOKIE():
    pass

def ensure_loged_in(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        username = bottle.request.get_cookie(COOKIE,
            secret=secret(bottle.request)
        )
        if username is not None:
            kwargs['username'] = username
            return function(*args, **kwargs)
        return bootle.redirect('/login')

    return wrapper

@application.post("/mailinglists/add")
@Web.ensure_logged_in
def person_add_submit(username):
    name = bottle.request.forms.get("name")
    
    try:
        idk = Data.MailingList.add(name)
        bottle.redirect("/mailinglists/view")
    except Data.Sql.Erro as err:
        return bottle.mako_template("error", url='/mailinglists/add',
            text="Add Mailinglist", message=str(err))

@float_args_and_return
def mean(first, second, *rest):
    numbers = (first, second) + rest
    return sum(numbers) / len(numbers)


@statically_typed(str, str, return_type=str)
def make_tagged(text, tag):
    return "<{0}>{1}</{0}>".format(tag, escape(text))


@statically_typed(str, int, str) # Will accept any return type
def repeat(what, count, separator):
    return ((what + separator) * count)[:-len(separator)]

# End
