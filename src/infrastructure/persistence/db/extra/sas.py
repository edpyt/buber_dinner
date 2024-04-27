"""Sync as async decorator. Taken from here: https://github.com/sqlalchemy/sqlalchemy/discussions/5923#discussioncomment-353620"""

import greenlet
from sqlalchemy.util._concurrency_py3k import _AsyncIoGreenlet
from sqlalchemy.util.concurrency import await_only


def running_in_greenlet():
    return isinstance(greenlet.getcurrent(), _AsyncIoGreenlet)


def sync_as_async(fn):
    def go(*arg, **kw):
        if running_in_greenlet():
            return await_only(fn(*arg, **kw))
        else:
            # no greenlet, assume no event loop and blocking IO backend
            coro = fn(*arg, **kw)
            try:
                coro.send(None)
            except StopIteration as err:
                return err.value

    return go
