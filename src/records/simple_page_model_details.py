from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    # Open new page
    page = context.new_page()

    # Go to file:///C:/Projects/playwr/src/data/runtime_data.html#summary
    page.goto("file:///C:/Projects/playwr/src/data/runtime_data.html#summary")

    # Click text=Hailo Dataflow Compiler — Profiler Report
    page.locator("text=Hailo Dataflow Compiler — Profiler Report").click()

    # Click text=Auto-generated version 3.20.0.dev0 in Sun, 21 Aug 2022 16:51:38 +0300
    page.locator("text=Auto-generated version 3.20.0.dev0 in Sun, 21 Aug 2022 16:51:38 +0300").click()

    # Click h3:has-text("Summary")
    page.locator("h3:has-text(\"Summary\")").click()
    page.locator("h3:has-text(\"Summary\")").all_text_contents()
    # Click label:has-text("SIMPLE")
    page.locator("label:has-text(\"SIMPLE\")").click()

    # Click text=Model Details
    page.locator("text=Model Details").click()

    # Click text=Model Name
    page.locator("text=Model Name").click()

    # Click text=Input Tensors Shapes
    page.locator("text=Input Tensors Shapes").click()

    # Click text=Output Tensors Shapes
    page.locator("text=Output Tensors Shapes").click()

    # Click text=Operations per Input Tensor (OPs)
    page.locator("text=Operations per Input Tensor (OPs)").click()

    # Click text=Operations per Input Tensor (MACs)
    page.locator("text=Operations per Input Tensor (MACs)").click()

    # Click text=Model Parameters
    page.locator("text=Model Parameters").click()

    # Click text=mobilenet_v2_1_4
    page.locator("text=mobilenet_v2_1_4").click()

    # Click text=224x224x3
    page.locator("text=224x224x3").click()

    # Click text=1x1x1001
    page.locator("text=1x1x1001").click()

    # Click text=1.2 GOPs
    page.locator("text=1.2 GOPs").click()

    # Click text=6.1 M
    page.locator("text=6.1 M").click()

    # Click text=0.6 GMACs
    page.locator("text=0.6 GMACs").click()


    # ---------------------
    page.close()
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
