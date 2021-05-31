#include <gtk/gtk.h>

GtkWidget *signup_username, *signup_password;
// stores the username and the password

static void print_hello(GtkWidget *widget,gpointer data){
	const gchar* username = gtk_entry_get_text(GTK_ENTRY(signup_username));
}

static void activate(GtkApplication *app,gpointer user_data){
	GtkWidget *window;
	GtkWidget *grid;
	GtkWidget *signup_button;
	GtkWidget *signin_button;
	GtkWidget *signup_username_label;
	GtkWidget *signup_password_label;

	window = gtk_application_window_new(app);
	gtk_window_set_title(GTK_WINDOW(window), "Sign Up");

	// constructing the grid here
	grid = gtk_grid_new();
	// pack the container in the window
	gtk_window_set_child(GTK_WINDOW(window), grid);

	// sign up
	signup_username_label = gtk_label_new("Username");
	signup_username = gtk_entry_new();
	signup_password_label = gtk_label_new("Password");
	signup_password = gtk_entry_new();
	gtk_grid_attach(GTK_GRID(grid), signup_username_label, 0,0,1,1);
	gtk_grid_attach(GTK_GRID(grid), signup_password_label, 0,1,1,1);
	gtk_grid_attach(GTK_GRID(grid), signup_username, 1,0,1,1);
	gtk_grid_attach(GTK_GRID(grid), signup_password, 1,1,1,1);

	// sign up button
	signup_button = gtk_button_new_with_label("Sign Up");
	g_signal_connect(signup_button, "clicked", G_CALLBACK (print_hello), NULL);
	gtk_grid_attach(GTK_GRID(grid), signup_button, 0,5,1,1);

	// sign in button
	signin_button = gtk_button_new_with_label("Sign In");
	g_signal_connect(signin_button, "clicked", G_CALLBACK (print_hello), NULL);
	gtk_grid_attach(GTK_GRID(grid), signin_button, 1,5,1,1);




	gtk_widget_show(window);
}

int main(int argc, char **argv){
  GtkApplication *app;
  int status;

  app = gtk_application_new ("org.gtk.example", G_APPLICATION_FLAGS_NONE);
  g_signal_connect (app, "activate", G_CALLBACK (activate), NULL);
  status = g_application_run (G_APPLICATION (app), argc, argv);
  g_object_unref (app);

  return status;
}
