from shiny import App, render, ui
import pandas as pd
import seaborn as sns
import warnings
from pathlib import Path

sns.set_theme()

long_breeds = pd.read_csv(Path(__file__).parent / "dog_traits_long.csv")

options_traits = long_breeds["trait"].unique().tolist()
options_breeds = long_breeds["breed"].unique().tolist()

app_ui = ui.page_fluid(
    ui.input_selectize("traits", "Traits", options_traits, multiple=True),
    ui.input_selectize("breeds", "Breeds", options_breeds, multiple=True),
    ui.output_plot("barchart"),
)


def server(input, output, session):
    @output
    @render.plot
    def barchart():
        # note that input.traits() refers to the traits selected via the UI
        indx_trait = long_breeds["trait"].isin(input.traits())
        indx_breed = long_breeds["breed"].isin(input.breeds())

        # subset data to keep only selected traits and breeds
        sub_df = long_breeds[indx_trait & indx_breed]

        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            # we'll set a dummy value for x, and use hue in the barchart.
            sub_df["dummy"] = 1

        # plot data
        g = sns.catplot(
            data=sub_df,
            kind="bar",
            y="rating",
            x="dummy",
            hue="trait",
            col="breed",
            col_wrap=4,
        )

        # remove labels on x-axis, which is on the legend anyway
        g.set_xlabels("")
        g.set_xticklabels("")
        g.set_titles(col_template="{col_name}")

        return g


app = App(app_ui, server)
