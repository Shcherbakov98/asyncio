"""Реализация задачи"""
from chapter_14.listing_14_08 import CustomFuture


class CustomTask(CustomFuture):
    def __init__(self, coro, loop):
        super(CustomFuture, self).__init__()
        self._coro = coro
        self._loop = loop
        self._current_result = None
        self._task_state = None
        loop.register_task(self)  # зарегистрировать задачу в цикле событий

    # выполнить один шаг сопрограммы
    def step(self):
        try:
            if self._task_state is None:
                self._task_state = self._coro.send(None)
            # если сопрограмма отдает future, вызвать add_done_callback
            if isinstance(self._task_state, CustomFuture):
                self._task_state.add_done_callback(self._future_done)
        except StopIteration as si:
            self.set_result(si.value)

    def _future_done(self, result):
        self._current_result = result
        try:
            self._task_state = self._coro.send(self._current_result)
        except StopIteration as si:
            self.set_result(si.value)
