from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, devtools=True)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to file:///C:/Projects/playwr/src/data/runtime_data.html
    page.goto("file:///C:/Projects/playwr/src/data/runtime_data.html")

    # Click text=Hailo Dataflow Compiler — Profiler ReportAuto-generated version 3.20.0.dev0 in S
    page.locator("text=Hailo Dataflow Compiler — Profiler ReportAuto-generated version 3.20.0.dev0 in S").click()

    # Other important methods:
    # page.click("a:has-text(\"Summary\")")
    # Fill div > input >> nth=0
    # page.locator("div > input").first.fill("conv")
    # Press Enter
    # page.locator("div > input").first.press("Enter")
    # https: // playwright.dev / python / docs / writing - tests

    # Click a:has-text("Summary")
    page.locator("TotalUtilizationSimple-title").click()
    page.wait_for_url("file:///C:/Projects/playwr/src/data/runtime_data.html#summary")

    # Click text=SummaryModel DetailsModel Namemobilenet_v2_1_4Input Tensors Shapes224x224x3Outpu
    page.locator("text=SummaryModel DetailsModel Namemobilenet_v2_1_4Input Tensors Shapes224x224x3Outpu").click()

    # Click a:has-text("Device Utilization")
    page.locator("a:has-text(\"Device Util\")").click()
    page.wait_for_url("file:///C:/Projects/playwr/src/data/runtime_data.html#deviceUtilization")

    # Click text=Device Utilization SimpleTotal UtilizationCompute Usage+40.23 %Compute Usage: 40
    page.locator("text=Device Utilization SimpleTotal UtilizationCompute Usage+40.23 %Compute Usage: 40").click()

    # Click a:has-text("Optimization")
    page.locator("a:has-text(\"Optimization\")").click()
    page.wait_for_url("file:///C:/Projects/playwr/src/data/runtime_data.html#optimization")

    # Click text=OptimizationModel OptimizationOptimization LevelN/ACompression LevelN/ARatio of
    page.locator("text=OptimizationModel OptimizationOptimization LevelN/ACompression LevelN/ARatio of ").click()

    # Click text=DETAILED
    page.locator("text=DETAILED").click()

    # Click text=Device Utilization DetailedNumber of contexts used for allocation: 1Total Utiliz
    page.locator("text=Device Utilization DetailedNumber of contexts used for allocation: 1Total Utiliz").click()

    # Click a:has-text("Summary")
    page.locator("a:has-text(\"Summary\")").click()
    page.wait_for_url("file:///C:/Projects/playwr/src/data/runtime_data.html#summary")

    # Click text=SummaryModel DetailsModel Namemobilenet_v2_1_4Input Tensors Shapes224x224x3Outpu
    page.locator("text=SummaryModel DetailsModel Name").click()

    # Click a:has-text("Device Utilization")
    page.locator("a:has-text(\"Device Utilization\")").click()
    page.wait_for_url("file:///C:/Projects/playwr/src/data/runtime_data.html#deviceUtilization")

    # Click text=Device Utilization DetailedNumber of contexts used for allocation: 1Total Utiliz
    page.locator("text=Device Utilization DetailedNumber of contexts used for allocation: 1Total Utiliz").click()

    # Click a:has-text("Optimization")
    page.locator("a:has-text(\"Optimization\")").click()
    page.wait_for_url("file:///C:/Projects/playwr/src/data/runtime_data.html#optimization")

    # Click text=OptimizationModel OptimizationOptimization LevelN/ACompression LevelN/ARatio of
    page.locator("text=OptimizationModel OptimizationOptimization LevelN/ACompression LevelN/ARatio of ").click()

    # Click a:has-text("Model Description")
    page.locator("a:has-text(\"Model Description\")").click()
    page.wait_for_url("file:///C:/Projects/playwr/src/data/runtime_data.html#modelDescription")

    # Click text=Model DescriptionLayer NameLayer TypeInput [W×H]Kernel [W×H]Strides [W×H]Feature
    page.locator("text=Model DescriptionLayer NameLayer TypeInput [W×H]Kernel [W×H]Strides [W×H]Feature").click()

    # Click a:has-text("NN Core Execution Simulation")
    page.locator("a:has-text(\"NN Core Execution Simulation\")").click()
    page.wait_for_url("file:///C:/Projects/playwr/src/data/runtime_data.html#latency")

    # Click text=NN Core Execution SimulationThis diagram visualizes the flow of three tensors (f
    page.locator("text=NN Core Execution SimulationThis diagram visualizes the flow of three tensors (f").click()

    # Click a:has-text("Model Graph")
    page.locator("a:has-text(\"Model Graph\")").click()
    page.wait_for_url("file:///C:/Projects/playwr/src/data/runtime_data.html#graph")

    # Click text=Model GraphUse Ctrl + Mouse Wheel for Zoom In/Zoom OutLayer parametersLayer Name
    page.locator("text=Model GraphUse Ctrl + Mouse Wheel for Zoom In/Zoom OutLayer parametersLayer Name").click()

    # Click text=Model GraphUse Ctrl + Mouse Wheel for Zoom In/Zoom Outinput_layer1norm_layer1con >> button >> nth=2
    page.locator("text=Model GraphUse Ctrl + Mouse Wheel for Zoom In/Zoom Outinput_layer1norm_layer1con >> button").nth(2).click()

    # Click text=RUNTIME
    page.locator("text=RUNTIME").click()

    # Click a:has-text("Latency Breakdown")
    page.locator("a:has-text(\"Latency Breakdown\")").click()
    page.wait_for_url("file:///C:/Projects/playwr/src/data/runtime_data.html#contextsLatency")

    # Click text=Latency BreakdownPreliminaryConfig TimeInfer, Drain TimeOverhead TimeLoad Timepr
    page.locator("text=Latency BreakdownPreliminaryConfig TimeInfer, Drain TimeOverhead TimeLoad Timepr").click()

    # Click text=Hailo Dataflow Compiler — Profiler ReportAuto-generated version 3.20.0.dev0 in S
    page.locator("text=Hailo Dataflow Compiler — Profiler ReportAuto-generated version 3.20.0.dev0 in S").click()

    # Click text=Auto-generated version 3.20.0.dev0 in Sun, 21 Aug 2022 16:51:38 +0300
    page.locator("text=Auto-generated version 3.20.0.dev0 in Sun, 21 Aug 2022 16:51:38 +0300").click()

    # Click text=Auto-generated version 3.20.0.dev0 in Sun, 21 Aug 2022 16:51:38 +0300
    page.locator("text=Auto-generated version 3.20.0.dev0 in Sun, 21 Aug 2022 16:51:38 +0300").click(button="right")

    # Click text=Hailo Dataflow Compiler — Profiler ReportAuto-generated version 3.20.0.dev0 in S
    page.locator("text=Hailo Dataflow Compiler — Profiler ReportAuto-generated version 3.20.0.dev0 in S").click()

    # ---------------------
    context.close()
    browser.close()

if __name__ == "__main__":
    # Playwright demo
    with sync_playwright() as playwright:
        run(playwright)
