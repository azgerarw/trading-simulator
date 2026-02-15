from tkinter import messagebox

from backend.models.profile.user_history.types import Types
from backend.models.users.user import User
import backend.users.state as state
from frontend.views.profile.view import View

class ProfilePresenter:

    def __init__(self, container, root, pages):
        self.container = container
        self.root = root
        self.pages = pages
        self.view = View(container=self.container, root=self.root, pages=self.pages)
        self.view.layout_frame1.navbar.on_select = self.on_selected_option
        self.view.layout_frame2.on_filter_selected = self.check
        self.view.layout_frame2.delete_account = self.delete

        self.container.grid(row=0, column=0, sticky="nsew")

        self.container.rowconfigure(0, weight=1)
        self.container.columnconfigure(0, weight=1)

        self.container.rowconfigure(1, weight=20)

    def on_selected_option(self, value):

        self.view.layout_frame1.navbar.check_option(value, self.pages)


    def check(self, value):
        if value == "trades":
            
            user_id = state.current_user[0]

            trades = Types().fetch_trades(user_id=user_id)

            Types().build_trades(self.view.layout_frame2.trades_container, trades)

            self.view.layout_frame2.trades_frame.tkraise()

        elif value == "deposits":

            user_id = state.current_user[0]

            deps = Types().fetch_deposits(user_id=user_id)

            Types().build_deposits(deposits_frame=self.view.layout_frame2.deposits_container, deposits=deps)

            self.view.layout_frame2.deposits_frame.tkraise()
        else:

            user_id = state.current_user[0]

            withdrawals = Types().fetch_withdrawals(user_id=user_id)

            Types().build_withdrawals(withdrawals_frame=self.view.layout_frame2.withdrawals_container, withdrawals=withdrawals)

            self.view.layout_frame2.withdrawals_frame.tkraise()

    def delete(self):
        
        result = messagebox.askokcancel(title='delete account', message='confirm to delete your account?', detail='account will be deleted and all data related to it')

        if result:

            user = User()
            user.delete(user_id=state.current_user[0])

            messagebox.showinfo('Account deleted', 'account successfully deleted')

            self.pages["login"][0].tkraise()